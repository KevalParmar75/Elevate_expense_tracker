def get_expense():
  while True:
    try:
      amount = float(input("Enter amount (e.g., 10.50): "))
      category = input("Enter category (e.g., Food, Groceries): ")
      return {"amount": amount, "category": category}
    except ValueError:
      print("Invalid input. Please enter a number for amount.")

def calculate_total(expenses):
  total = 0
  for expense in expenses:
    total += expense["amount"]
  return total

def summarize_by_category(expenses):
  summary = {}
  for expense in expenses:
    category = expense["category"]
    if category in summary:
      summary[category] += expense["amount"]
    else:
      summary[category] = expense["amount"]
  return summary

def main():
  expenses = []

  while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
      expenses.append(get_expense())
    elif choice == '2':
      total = calculate_total(expenses)
      summary = summarize_by_category(expenses)
      print("\nTotal Expenses:", total)
      for category, amount in summary.items():
        print(f"{category}: {amount:.2f}")
    elif choice == '3':
      print("Exiting Expense Tracker.")
      break
    else:
      print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
  main()
