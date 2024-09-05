while True:
    try:
        f = input("How much fuel is in the tank (X/Y)? ")
        f1, f2 = map(int, f.split("/"))
        if (f1 > f2):
            continue
        fuel = round(f1 / f2, 2)
        break
    except ValueError:
        print("Invalid arguments")

    except ZeroDivisionError:
        print("Division by zero")

if fuel <= 0.01:
    print("E")
elif fuel >=0.99:
    print("F")
else:
    print(f"{fuel:.0%}")