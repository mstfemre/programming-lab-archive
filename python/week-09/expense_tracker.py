from datetime import datetime


ALLOWED_CATEGORIES = {"Food", "Transport", "Bills", "Entertainment"}


def add_expense(**kwargs):
    try:
        description = kwargs["description"]
        amount = kwargs["amount"]
        category = kwargs["category"]

        if not isinstance(description, str) or not description.strip():
            raise ValueError("Description must be a non-empty string.")

        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        if not isinstance(category, str) or category not in ALLOWED_CATEGORIES:
            allowed = ", ".join(sorted(ALLOWED_CATEGORIES))
            raise ValueError(f"Category must be one of: {allowed}.")

    except KeyError as error:
        raise ValueError(f"Missing required field: {error.args[0]}.")

    return {
        "description": description.strip(),
        "amount": float(amount),
        "category": category,
        "date": datetime.now(),
    }


def days_ago(expense_date):
    if not isinstance(expense_date, datetime):
        raise ValueError("Expense date must be a datetime object.")

    return (datetime.now() - expense_date).days


def print_expenses(title, expenses_list):
    print(f"\n{title}")

    if not expenses_list:
        print("No expenses found.")
        return

    for expense in expenses_list:
        print(
            f"{expense['description']} | "
            f"{expense['category']} | "
            f"{expense['amount']:.2f} | "
            f"{expense['date'].strftime('%Y-%m-%d')} | "
            f"{days_ago(expense['date'])} days ago"
        )


def sort_by_amount(expenses_list):
    sorted_expenses = sorted(
        expenses_list,
        key=lambda expense: expense["amount"],
        reverse=True,
    )
    print_expenses("Expenses sorted by amount:", sorted_expenses)
    return sorted_expenses


def filter_last_week(expenses_list):
    recent_expenses = list(
        filter(lambda expense: days_ago(expense["date"]) <= 7, expenses_list)
    )
    print_expenses("Expenses from the last 7 days:", recent_expenses)
    return recent_expenses


def find_common_categories(expenses_list):
    categories = [expense["category"] for expense in expenses_list]
    unique_categories = set(categories)
    common_categories = {
        category for category in unique_categories if categories.count(category) >= 2
    }
    return common_categories


def summary(expenses_list):
    total_expenses = len(expenses_list)
    total_amount = sum(expense["amount"] for expense in expenses_list)
    average_amount = round(total_amount / total_expenses, 2) if total_expenses else 0
    unique_categories = {expense["category"] for expense in expenses_list}

    print("\nExpense Summary")
    print(f"Total number of expenses: {total_expenses}")
    print(f"Total amount spent: {total_amount:.2f}")
    print(f"Average amount: {average_amount:.2f}")
    print(f"Unique categories: {', '.join(sorted(unique_categories))}")


expenses = []

# Successful registrations
expenses.append(add_expense(description="Groceries", amount=85.50, category="Food"))
expenses.append(add_expense(description="Bus ticket", amount=12.00, category="Transport"))
expenses.append(add_expense(description="Coffee", amount=4.75, category="Food"))
expenses.append(add_expense(description="Electric bill", amount=120.00, category="Bills"))

# This should raise an error
try:
    add_expense(description="", amount=-10, category="Books")
except ValueError as e:
    print(f"Registration failed: {e}")

sort_by_amount(expenses)
summary(expenses)
filter_last_week(expenses)
common_categories = find_common_categories(expenses)
print(f"\nCommon categories: {', '.join(sorted(common_categories))}")
