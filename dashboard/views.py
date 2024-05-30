from django.shortcuts import render
from debt_manager.models import Debt, Debtor, ExchangeRate
from debt_manager import utilites as U

# Create your views here.


def dashboard(request):
    out = {}
    out = U.prepare_content_data(out)
    debt_list = Debt.objects.filter(is_closed=False)
    # print(debt_list)
    out['debt_list'] = debt_list.order_by('date_end')
    return render(request, 'dashboard/dashboard.html', out)
