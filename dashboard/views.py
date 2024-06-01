from django.shortcuts import render
from debt_manager.models import Debt, Debtor, ExchangeRate
from debt_manager import utilites as U

# Create your views here.


def dashboard(request):
    out = {}
    out = U.prepare_content_data(out)
    debt_list = Debt.objects.filter(is_closed=False)
    debtors = Debtor.objects.filter(debt__is_closed=False).distinct().order_by('last_name')
    debtor_list = debtors.values()
    for debtor in debtor_list:
        debtor['debts'] = debt_list.filter(debtor_id=debtor['id'])

    out['debtor_list'] = debtor_list
    return render(request, 'dashboard/dashboard.html', out)
