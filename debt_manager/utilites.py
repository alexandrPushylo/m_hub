import debt_manager.assets as ASSETS
from debt_manager.models import Debt, Debtor, ExchangeRate
from datetime import date, timedelta, datetime
import time
import random

TODAY = date.today()
NOW = datetime.now().time()


def get_transaction_count(debtor: Debtor) -> int:
    count = Debt.objects.filter(debtors=debtor).count()
    return count


def prepare_content_data(context=None) -> dict:
    if context is None:
        context = {}
    context['TODAY'] = TODAY
    context['NOW'] = NOW
    return context
