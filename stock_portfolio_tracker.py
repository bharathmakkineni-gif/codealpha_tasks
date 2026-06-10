stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

total_value = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    value = stock_prices[stock] * quantity
    total_value += value

print("\nTotal Investment Value: $", total_value)

with open("portfolio_report.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_value}")

print("Report saved as portfolio_report.txt")