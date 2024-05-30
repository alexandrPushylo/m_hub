from django.shortcuts import render
from debt_manager.models import Debt, Debtor, ExchangeRate
# Create your views here.

# def main_card(request):
#     out = {}
#     debt_list = Debt.objects.all()
#     print(debt_list)
#     out['debt_list'] = debt_list
#     return render(request, 'debt_manager/debt_manager_card.html', out)
