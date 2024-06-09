from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from debt_manager.models import Debt, Debtor, ExchangeRate
import debt_manager.assets as ASSETS
import debt_manager.utilites as U
import debt_manager.endpoints as ENDPOINTS


# Create your views here.

def edit_debt_view(request):
    out = {
        'currency_list': ASSETS.CURRENCY_CHOICES
    }
    out = U.prepare_content_data(out)

    debtor_list = Debtor.objects.filter()
    out['debtor_list'] = debtor_list

    debt_id = request.GET.get('debt_id')
    if debt_id:
        debt = Debt.objects.get(pk=debt_id)
        debtor = debtor_list.get(pk=debt.debtor.pk)
        out['debtor'] = debtor
        out['debt'] = debt

    debtor_id = request.GET.get('debtor_id')
    if debtor_id:
        debtor = debtor_list.get(pk=debtor_id)
        out['debtor'] = debtor

    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        date_start_time = request.POST.get('date_start_time')
        date_start_date = request.POST.get('date_start_date')
        date_end = request.POST.get('date_end')

        if date_end == '':
            date_end = None

        if last_name and first_name:
            _debtor, _ = Debtor.objects.get_or_create(
                last_name=last_name,
                first_name=first_name
            )
            _debt = Debt.objects.create(
                title=title,
                description=description,
                amount=amount,
                currency=currency,
                date_start_time=date_start_time,
                date_start_date=date_start_date,
                date_end=date_end,
                debtor=_debtor
            )
        return HttpResponseRedirect(ENDPOINTS.DASHBOARD)

    return render(request, 'debt_manager/edit_debt.html', out)


def personal_debt_view(request):
    out = {}
    out = U.prepare_content_data(out)

    if request.method == 'POST':
        debt_id = request.POST.get('debt_id')
        if debt_id:
            _dept = Debt.objects.get(pk=debt_id)
            _dept.is_closed = False if _dept.is_closed else True
            _dept.save()

    debtor_id = request.GET.get('debtor_id')
    if debtor_id:
        debtor = Debtor.objects.get(pk=debtor_id)
        debt_list = Debt.objects.filter(debtor=debtor)

        out['debtor'] = debtor
        out['debt_list'] = debt_list
        print(debtor)
        print(debt_list)

    return render(request, 'debt_manager/personal_debt.html', out)
