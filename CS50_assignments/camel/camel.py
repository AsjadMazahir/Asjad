def main():
    name = input("Name in camel case: ")
    snake_case = snake(name)
    print(snake_case)

def snake(name):
    for c in name:
        if c.isupper():
            name = name.replace(c, f"_{c.lower()}")

    return name


if __name__ == "__main__":
    main()