from pathlib import Path
import pandas as pd


REQUIRED_COLUMNS = ["date", "type", "amount", "category", "description"]


def load_transactions(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    elif path.suffix.lower() in [".xlsx", ".xls"]:
        df = pd.read_excel(path)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")

    if df.empty:
        return pd.DataFrame(columns=REQUIRED_COLUMNS)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in file: {missing}")

    return df[REQUIRED_COLUMNS]


def save_transactions(df: pd.DataFrame, file_path: str) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.suffix.lower() == ".csv":
        df.to_csv(path, index=False)
    elif path.suffix.lower() in [".xlsx", ".xls"]:
        df.to_excel(path, index=False)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")
