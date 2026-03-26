from src.constants import DEFAULT_CATEGORIES
from src.file_handler import load_transactions, save_transactions
from src.reports import monthly_summary
from src.tracker import ExpenseTracker
from src.visualizer import plot_expense_bar, plot_expense_pie


def print_menu() -> None:
    print("\n=== Expense Tracker ===")
    print("1. Add income/expense")
    print("2. View all transactions")
    print("3. Show balance")
    print("4. Filter by category")
    print("5. Search by date/category")
    print("6. Monthly summary")
    print("7. Show charts")
    print("8. Save data")
    print("9. Load data")
    print("0. Exit")


def main() -> None:
    data_file = "data/transactions.csv"
    tracker = ExpenseTracker(load_transactions(data_file))

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                date = input("Date (YYYY-MM-DD): ")
                tx_type = input("Type (income/expense): ")
                amount = input("Amount: ")
                print(f"Suggested categories: {', '.join(DEFAULT_CATEGORIES)}")
                category = input("Category: ")
                description = input("Description: ")
                tracker.add_transaction(date, tx_type, amount, category, description)
                print("Transaction added successfully.")

            elif choice == "2":
                df = tracker.view_transactions()
                print(df.to_string(index=False) if not df.empty else "No transactions found.")

            elif choice == "3":
                print(f"Current Balance: {tracker.get_balance():.2f}")

            elif choice == "4":
                category = input("Category to filter: ")
                df = tracker.filter_by_category(category)
                print(df.to_string(index=False) if not df.empty else "No matching transactions.")

            elif choice == "5":
                category = input("Category (optional, press Enter to skip): ").strip() or None
                date = input("Date YYYY-MM-DD (optional, press Enter to skip): ").strip() or None
                df = tracker.search(category=category, date=date)
                print(df.to_string(index=False) if not df.empty else "No matching transactions.")

            elif choice == "6":
                summary = monthly_summary(tracker.transactions)
                print(summary.to_string(index=False) if not summary.empty else "No data available.")

            elif choice == "7":
                chart_type = input("Chart type (pie/bar): ").strip().lower()
                if chart_type == "pie":
                    plot_expense_pie(tracker.transactions)
                elif chart_type == "bar":
                    plot_expense_bar(tracker.transactions)
                else:
                    print("Invalid chart type.")

            elif choice == "8":
                path = input("Save path (CSV or Excel): ").strip() or data_file
                save_transactions(tracker.transactions, path)
                print(f"Data saved to {path}")

            elif choice == "9":
                path = input("Load path (CSV or Excel): ").strip() or data_file
                tracker = ExpenseTracker(load_transactions(path))
                print(f"Data loaded from {path}")

            elif choice == "0":
                save_transactions(tracker.transactions, data_file)
                print("Data auto-saved. Goodbye.")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
