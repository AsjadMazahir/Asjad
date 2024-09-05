import random

def main():
    level = get_level()
    correct = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        if check_answer(x, y):
            correct += 1
    print(f"Score: {correct}")

# prompts the user for level
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in range(1, 4):
                return n
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    start = 10 ** (level-1)
    stop = 10 ** level - 1

    if level == 1:
        start -= 1

    return random.randint(start, stop)

def check_answer(x, y):
    for _ in range(3):
        try:
            prompt = input(f"{x} + {y} = ")
            if int(prompt) == (x + y):
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
            continue

    print(f"{x} + {y} = {x+y}")
    return False
if __name__ == "__main__":
    main()