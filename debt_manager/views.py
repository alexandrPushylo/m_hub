from django.shortcuts import render
from debt_manager.models import Debt, Debtor, ExchangeRate
import debt_manager.assets as ASSETS


# Create your views here.

def edit_debt_view(request):
    out = {
        'currency_list': ASSETS.CURRENCY_CHOICES
    }
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        date_start = request.POST.get('date_start')
        date_end = request.POST.get('date_end')
        
    return render(request, 'debt_manager/edit_debt.html', out)
