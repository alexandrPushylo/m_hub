from django.shortcuts import render
from bills.models import Electricity, ColdWater, HotWater, Rent
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


def edit_cold_water(request):
    template = 'bills/edit_cold_water.html'
    context = {
        'title': 'Холодная вода'
    }
    last_cold_water = ColdWater.objects.filter(payment_date__month=U.MONTH - 1)
    current_cold_water = ColdWater.objects.filter(payment_date__month=U.MONTH)

    if request.method == 'POST':
        indications = request.POST.get('current_indications')
        amount = request.POST.get('amount')
        rate = request.POST.get('rate')
        payment_date = request.POST.get('payment_date', U.TODAY)
        description = request.POST.get('description')

        if all([indications, amount, rate, payment_date]):
            electricity, _ = ColdWater.objects.update_or_create(payment_date__month=U.MONTH, defaults={
                'indications': indications,
                'amount': amount,
                'rate': rate,
                'payment_date': payment_date,
                'description': description
            })
        return HttpResponseRedirect(ENDPOINTS.DASHBOARD)
    if last_cold_water.exists():
        rate = last_cold_water.first().rate
        last_indications = last_cold_water.first().indications
    else:
        rate = 0
        last_indications = 0

    if current_cold_water.exists():
        current_indications = current_cold_water.first().indications
        description = current_cold_water.first().description
        amount = current_cold_water.first().amount
        payment_date = current_cold_water.first().payment_date

        context['amount'] = str(amount).replace(',', '.')
        context['description'] = description
        context['current_indications'] = current_indications
        context['indications_diff'] = current_indications - last_indications
    else:
        payment_date = U.TODAY

    context['payment_date'] = payment_date
    context['last_indications'] = last_indications
    context['rate'] = str(rate).replace(',', '.')

    return render(request, template, context)


def edit_hot_water(request):
    template = 'bills/edit_hot_water.html'
    context = {
        'title': 'Горячая вода'
    }
    last_hot_water = HotWater.objects.filter(payment_date__month=U.MONTH - 1)
    current_hot_water = HotWater.objects.filter(payment_date__month=U.MONTH)

    if request.method == 'POST':
        indications = request.POST.get('current_indications')
        amount = request.POST.get('amount')
        rate = request.POST.get('rate')
        payment_date = request.POST.get('payment_date', U.TODAY)
        description = request.POST.get('description')

        if all([indications, amount, rate, payment_date]):
            electricity, _ = HotWater.objects.update_or_create(payment_date__month=U.MONTH, defaults={
                'indications': indications,
                'amount': amount,
                'rate': rate,
                'payment_date': payment_date,
                'description': description
            })
        return HttpResponseRedirect(ENDPOINTS.DASHBOARD)
    if last_hot_water.exists():
        rate = last_hot_water.first().rate
        last_indications = last_hot_water.first().indications
    else:
        rate = 0
        last_indications = 0

    if current_hot_water.exists():
        current_indications = current_hot_water.first().indications
        description = current_hot_water.first().description
        amount = current_hot_water.first().amount
        payment_date = current_hot_water.first().payment_date

        context['amount'] = str(amount).replace(',', '.')
        context['description'] = description
        context['current_indications'] = current_indications
        context['indications_diff'] = current_indications - last_indications
    else:
        payment_date = U.TODAY

    context['payment_date'] = payment_date
    context['last_indications'] = last_indications
    context['rate'] = str(rate).replace(',', '.')

    return render(request, template, context)


def edit_rent(request):
    template = 'bills/edit_rent.html'
    context = {
        'title': 'Квартплата'
    }
    last_rent = Rent.objects.filter(payment_date__month=U.MONTH - 1)
    current_rent = Rent.objects.filter(payment_date__month=U.MONTH)

    if request.method == 'POST':
        diff_amount = request.POST.get('diff_amount')
        current_amount = request.POST.get('current_amount')
        payment_date = request.POST.get('payment_date', U.TODAY)
        description = request.POST.get('description')

        if all([current_amount, payment_date]):
            electricity, _ = Rent.objects.update_or_create(payment_date__month=U.MONTH, defaults={
                'amount': current_amount,
                'payment_date': payment_date,
                'description': description
            })
        return HttpResponseRedirect(ENDPOINTS.DASHBOARD)
    if last_rent.exists():
        last_amount = last_rent.first().amount

    else:
        last_amount = 0

    if current_rent.exists():
        description = current_rent.first().description
        current_amount = current_rent.first().amount
        payment_date = current_rent.first().payment_date

        context['current_amount'] = str(current_amount).replace(',', '.')
        context['description'] = description
        context['diff_amount'] = current_amount - last_amount
    else:
        payment_date = U.TODAY

    context['payment_date'] = payment_date
    context['last_amount'] = str(last_amount).replace(',', '.')

    return render(request, template, context)
