stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 350
}

portfolio = {}
total_investment = 0

print("Enter your stock holdings.")
print("Type 'done' when you are finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
    if stock == 'DONE':
        break
    if stock == '':
        print("No input detected, try again.")
        continue
    if stock not in stock_prices:
        print("Stock not found in the price list. Try again.")
        continue
    try:
        quantity_input = input(f"Enter quantity of {stock}: ").strip()
        quantity = int(quantity_input)
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter an integer.")

print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares @ ${stock_prices[stock]} = ${value}")
    total_investment += value

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to a file
save_option = input("\nDo you want to save the result to a file? (yes/no): ").strip().lower()

if save_option == 'yes':
    file_choice = input("Choose file type - txt or csv: ").strip().lower()
    if file_choice == 'txt':
        with open('portfolio.txt', 'w') as file:
            for stock, quantity in portfolio.items():
                file.write(f"{stock}: {quantity} shares @ ${stock_prices[stock]} = ${stock_prices[stock]*quantity}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("Portfolio saved to portfolio.txt")
    elif file_choice == 'csv':
        import csv
        with open('portfolio.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Stock', 'Quantity', 'Price per Share', 'Total Value'])
            for stock, quantity in portfolio.items():
                writer.writerow([stock, quantity, stock_prices[stock], stock_prices[stock]*quantity])
            writer.writerow([])
            writer.writerow(['Total Investment', '', '', total_investment])
        print("Portfolio saved to portfolio.csv")
    else:
        print("Invalid file type selected. Skipping save.")

input("\nPress Enter to exit...")
