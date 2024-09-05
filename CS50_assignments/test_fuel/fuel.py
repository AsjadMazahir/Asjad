def main():
    f = input("How much fuel is in the tank (X/Y)? ")
    fract = convert(f)
    print(fract)
    per = gauge(fract)
    print(per)

def convert(fraction):
    try:
        f1, f2 = fraction.split("/")
        f1, f2 = int(f1), int(f2)

    except ValueError:
        raise ValueError("Invalid arguments")

    if f2 == 0:
        raise ZeroDivisionError("Division by zero not allowed")
    elif f1 > f2:
        raise ValueError("X cant be greater than Y")
    else:
        fuel = round(f1 / f2 * 100)
    return fuel

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()