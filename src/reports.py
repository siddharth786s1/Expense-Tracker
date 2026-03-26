import pandas as pd


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["month", "income", "expense", "net_balance"])

    data = df.copy()
    data["month"] = pd.to_datetime(data["date"]).dt.to_period("M").astype(str)

    income = (
        data[data["type"] == "income"]
        .groupby("month")["amount"]
        .sum()
        .rename("income")
    )
    expense = (
        data[data["type"] == "expense"]
        .groupby("month")["amount"]
        .sum()
        .rename("expense")
    )

    summary = pd.concat([income, expense], axis=1).fillna(0).reset_index()
    summary["net_balance"] = summary["income"] - summary["expense"]
    return summary.sort_values(by="month").reset_index(drop=True)
