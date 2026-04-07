from datetime import datetime
from typing import List

from src.schemas.account import AccountIn


class AccountService:
    def __init__(self) -> None:
        self._accounts: List[dict] = []
        self._next_id = 1

    async def read_all(self, limit: int, skip: int = 0):
        return self._accounts[skip : skip + limit]

    async def create(self, account: AccountIn):
        now = datetime.utcnow()
        account_data = {
            "id": self._next_id,
            "user_id": account.user_id,
            "balance": float(account.balance),
            "created_at": now,
        }
        self._next_id += 1
        self._accounts.append(account_data)
        return account_data
