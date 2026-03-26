import matplotlib.pyplot as plt
import pandas as pd


def plot_expense_pie(df: pd.DataFrame) -> None:
    expense_df = df[df["type"] == "expense"]
    if expense_df.empty:
        print("No expense data available for chart.")
        return

    by_category = expense_df.groupby("category")["amount"].sum()
    plt.figure(figsize=(7, 7))
    plt.pie(by_category.values, labels=by_category.index, autopct="%1.1f%%", startangle=140)
    plt.title("Expense Distribution by Category")
    plt.tight_layout()
    plt.show()


def plot_expense_bar(df: pd.DataFrame) -> None:
    expense_df = df[df["type"] == "expense"]
    if expense_df.empty:
        print("No expense data available for chart.")
        return

    by_category = expense_df.groupby("category")["amount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    by_category.plot(kind="bar")
    plt.ylabel("Amount")
    plt.title("Expense by Category")
    plt.tight_layout()
    plt.show()
