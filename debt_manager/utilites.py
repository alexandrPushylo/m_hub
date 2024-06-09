from debt_manager.models import Debt, Debtor
from datetime import date, datetime

TODAY = date.today
NOW = datetime.now().time
MONTH = datetime.now().month


def get_transaction_count(debtor: Debtor) -> int:
    count = Debt.objects.filter(debtors=debtor).count()
    return count


def prepare_content_data(context=None) -> dict:
    if context is None:
        context = {}
    context['TODAY'] = TODAY()
    context['NOW'] = NOW()
    return context
