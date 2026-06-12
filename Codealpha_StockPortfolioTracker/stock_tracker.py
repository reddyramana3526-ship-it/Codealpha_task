# Stock prices dictionary

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

# User input

stock_name = input("Enter stock name: ").upper()

quantity = int(input("Enter quantity: "))

# Check stock exists

if stock_name in stock_prices:

    price = stock_prices[stock_name]

    total = price * quantity

    print("Stock:", stock_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total)

    # Save result

    file = open("investment.txt", "w")

    file.write("Stock: " + stock_name + "\n")
    file.write("Price: " + str(price) + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment: " + str(total))

    file.close()

    print("Result saved in investment.txt")

else:
    print("Stock not found!")
    