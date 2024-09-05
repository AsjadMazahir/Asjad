# prompting for operation
expression = input("Enter mathematical expression: ").strip()
x, y, z = expression.split()
x, z = int(x), int(z)

if y == '+':
    print(f"{(x + z): .1f}")
elif y == '-':
    print(f"{(x - z): .1f}")
elif y == '*':
    print(f"{(x * z): .1f}")
elif y == '/':
    print(f"{(x / z): .1f}")
else:
    print("Invalid input")