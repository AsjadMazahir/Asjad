amount_required = 50
denominations = [5, 10, 25]
# prompting user for input
while True:
    coin = int(input("Enter amount: "))
    if coin in denominations:
        amount_required = amount_required - coin
    # checking the remaining amount
    if amount_required > 0:
        print("Amount due:", amount_required)

    elif amount_required <= 0:
        print(f"Change owed: {amount_required * -1}")
        break