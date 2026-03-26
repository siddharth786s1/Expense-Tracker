import pandas as pd
from src.constants import DEFAULT_CATEGORIES, TRANSACTION_TYPES
from src.utils import is_positive_number, is_valid_date


class ExpenseTracker:
    def __init__(self, initial_df: pd.DataFrame | None = None):
        self.transactions = (
            initial_df.copy()
            if initial_df is not None
            else pd.DataFrame(columns=["date", "type", "amount", "category", "description"])
        )

    def add_transaction(self, date: str, tx_type: str, amount: str, category: str, description: str) -> None:
        if not is_valid_date(date):
            raise ValueError("Invalid date. Use YYYY-MM-DD.")

        tx_type = tx_type.lower().strip()
        if tx_type not in TRANSACTION_TYPES:
            raise ValueError("Transaction type must be 'income' or 'expense'.")

        if not is_positive_number(amount):
            raise ValueError("Amount must be a positive number.")

        category = category.strip().title()
        if not category:
            category = "Other"

        if tx_type == "income":
            category = "Income"
        elif category not in DEFAULT_CATEGORIES and category != "Income":
            category = category

        row = {
            "date": date,
            "type": tx_type,
            "amount": float(amount),
            "category": category,
            "description": description.strip(),
        }
        self.transactions.loc[len(self.transactions)] = row

    def view_transactions(self) -> pd.DataFrame:
        return self.transactions.sort_values(by="date").reset_index(drop=True)

    def get_balance(self) -> float:
        income = self.transactions[self.transactions["type"] == "income"]["amount"].sum()
        expense = self.transactions[self.transactions["type"] == "expense"]["amount"].sum()
        return float(income - expense)

    def filter_by_category(self, category: str) -> pd.DataFrame:
        category = category.strip().title()
        return self.transactions[self.transactions["category"].str.title() == category].copy()

    def search(self, category: str | None = None, date: str | None = None) -> pd.DataFrame:
        df = self.transactions.copy()

        if category:
            df = df[df["category"].str.title() == category.strip().title()]

        if date:
            if not is_valid_date(date):
                raise ValueError("Invalid date. Use YYYY-MM-DD.")
            df = df[df["date"] == date]

        return df.reset_index(drop=True)
