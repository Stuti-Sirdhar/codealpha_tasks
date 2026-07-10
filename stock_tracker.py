# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

total_investment = 0

print("📊 Stock Investment Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"✅ Added: {stock} x {quantity} = {investment}")

print("\n💰 Total Investment Value:", total_investment)

# Optional: Save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("investment.txt", "w") as file:
        file.write(f"Total Investment: {total_investment}")
    print("📁 Saved to investment.txt")