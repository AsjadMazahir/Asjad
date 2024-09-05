from datetime import date, timedelta
import sys
import inflect


def main():
    d = input("Date of Birth: ")
    days = get_days(d)
    min = days * 24 * 60
    print(f"{convert_to_words(min)} minutes")

# Get number of days from date of birth till date
def get_days(d):
    try:
        year, month, day = map(int, d.split("-"))
        age = date.today() - date(year, month, day)
        return age.days

    except ValueError:
        sys.exit("Invalid date")

# convert minutes from numbers to word
def convert_to_words(days):
    p = inflect.engine()
    return (p.number_to_words(days, andword="")).capitalize()
if __name__ == "__main__":
    main()