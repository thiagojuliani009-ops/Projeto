from datetime import datetime
from typing import List

from src.schemas.transaction import TransactionIn


class TransactionService:
    def __init__(self) -> None:
        self._transactions: List[dict] = []
        self._next_id = 1

    async def read_all(self, account_id: int, limit: int, skip: int = 0):
        filtered = [tx for tx in self._transactions if tx["account_id"] == account_id]
        return filtered[skip : skip + limit]

    async def create(self, transaction: TransactionIn):
        now = datetime.utcnow()
        transaction_data = {
            "id": self._next_id,
            "account_id": transaction.account_id,
            "type": transaction.type,
            "amount": float(transaction.amount),
            "timestamp": now,
        }
        self._next_id += 1
        self._transactions.append(transaction_data)
        return transaction_data
