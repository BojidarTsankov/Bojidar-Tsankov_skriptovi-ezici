n = int(input("km = "))
daytime = str(input("Day/night: "))

if (n < 20):
    print("Taxi is the only way")

    if (daytime == 'day'):
        price = (0.79 * n) + 0.7
    elif (daytime == 'night'):
        price = (0.9 * n) + 0.7
    else:
        print("You didn't enter a valid daytime")

if (n >= 20 and n < 100):
    print("Bus is the only way")

    price = 0.09 * n

if (n > 100):
    print("Train is the only way")

    price = 0.06 * n

print(f"The price is {price}")
