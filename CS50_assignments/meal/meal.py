def main():
    time = input("What time is it? ")
    if convert("7:00") <= convert(time) <= convert("8:00"):
        print("breakfast time")
    elif convert("12:00") <= convert(time) <= convert("13:00"):
        print("lunch time")
    elif convert("18:00") <= convert(time) <= convert("19:00"):
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(':')
    time_new = int(hours) + int(minutes)/60
    return f"{time_new: .3f}"

if __name__ == "__main__":
    main()