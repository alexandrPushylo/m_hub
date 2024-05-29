import assets as ASSETS
from debt_manager.models import Debt, Debtor, ExchangeRate


def get_transaction_count(debtor: Debtor) -> int:
    count = Debt.objects.filter(debtors=debtor).count()
    return count

