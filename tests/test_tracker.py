import pytest
from src.tracker import ExpenseTracker


def test_add_and_balance():
    tracker = ExpenseTracker()
    tracker.add_transaction("2026-03-01", "income", "1000", "Salary", "Monthly pay")
    tracker.add_transaction("2026-03-02", "expense", "200", "Food", "Groceries")
    assert tracker.get_balance() == 800.0


def test_invalid_date():
    tracker = ExpenseTracker()
    with pytest.raises(ValueError):
        tracker.add_transaction("2026/03/01", "expense", "50", "Food", "Invalid")
