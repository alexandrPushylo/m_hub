from django.shortcuts import render
from bills.models import Electricity
from django.http import HttpResponseRedirect

import bills.utilites as U
import bills.endpoints as ENDPOINTS
# Create your views here.


def edit_electricity(request):
    context = {
        'title': 'Электроэнергия'
    }
    last_electricity = Electricity.objects.filter(payment_date__month=U.MONTH-1)
    current_electricity = Electricity.objects.filter(payment_date__month=U.MONTH)

    if request.method == 'POST':
        indications = request.POST.get('indications_diff')
        amount = request.POST.get('amount')
        rate = request.POST.get('rate')
        payment_date = request.POST.get('payment_date', U.TODAY)
        description = request.POST.get('description')

        if all([indications, amount, rate, payment_date]):
            electricity, _ = Electricity.objects.update_or_create(payment_date__month=U.MONTH, defaults={
                'indications': indications,
                'amount': amount,
                'rate': rate,
                'payment_date': payment_date,
                'description': description
            })
        return HttpResponseRedirect(ENDPOINTS.DASHBOARD)
    if last_electricity.exists():
        rate = last_electricity.first().rate
        last_indications = last_electricity.first().indications
    else:
        rate = 0
        last_indications = 0

    if current_electricity.exists():
        current_indications = current_electricity.first().indications
        description = current_electricity.first().description
        amount = current_electricity.first().amount
        payment_date = current_electricity.first().payment_date

        context['amount'] = str(amount).replace(',', '.')
        context['description'] = description
        context['current_indications'] = current_indications
        context['indications_diff'] = current_indications - last_indications
    else:
        payment_date = U.TODAY

    context['payment_date'] = payment_date
    context['last_indications'] = last_indications
    context['rate'] = str(rate).replace(',', '.')

    template = 'bills/edit_electricity.html'

    return render(request, template, context)
