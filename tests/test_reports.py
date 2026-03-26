import pandas as pd
from src.reports import monthly_summary


def test_monthly_summary():
    df = pd.DataFrame(
        [
            {"date": "2026-01-05", "type": "income", "amount": 1000, "category": "Income", "description": "Salary"},
            {"date": "2026-01-10", "type": "expense", "amount": 300, "category": "Food", "description": "Groceries"},
        ]
    )
    summary = monthly_summary(df)
    assert summary.iloc[0]["net_balance"] == 700
