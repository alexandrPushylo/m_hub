from django.shortcuts import render
from debt_manager.models import Debt, Debtor, ExchangeRate
from debt_manager import utilites as U
from bills.models import Electricity, ColdWater, HotWater, Rent, Gas

# Create your views here.


def dashboard(request):
    out = {}
    out = U.prepare_content_data(out)
    debt_list = Debt.objects.filter(is_closed=False, is_hidden=False)
    debtors = Debtor.objects.filter(debt__is_closed=False).distinct().order_by('last_name')
    debtor_list = debtors.values()
    for debtor in debtor_list:
        debtor['debts'] = debt_list.filter(debtor_id=debtor['id'])
    out['debtor_list'] = debtor_list

    electricity_list = Electricity.objects.filter(payment_date__month=U.MONTH)
    cold_water_list = ColdWater.objects.filter(payment_date__month=U.MONTH)
    hot_water_list = HotWater.objects.filter(payment_date__month=U.MONTH)
    rent_list = Rent.objects.filter(payment_date__month=U.MONTH)
    gas_list = Gas.objects.filter(payment_date__month=U.MONTH)

    out['electricity_list'] = electricity_list
    out['cold_water_list'] = cold_water_list
    out['hot_water_list'] = hot_water_list
    out['rent_list'] = rent_list
    out['gas_list'] = gas_list

    return render(request, 'dashboard/dashboard.html', out)
