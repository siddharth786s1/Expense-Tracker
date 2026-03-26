import pandas as pd
from src.file_handler import save_transactions, load_transactions


def test_save_and_load_csv(tmp_path):
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame(
        [{"date": "2026-03-01", "type": "expense", "amount": 120, "category": "Bills", "description": "Electricity"}]
    )
    save_transactions(df, str(file_path))
    loaded = load_transactions(str(file_path))
    assert len(loaded) == 1
    assert loaded.iloc[0]["category"] == "Bills"
