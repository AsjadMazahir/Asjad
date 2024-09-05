months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").title()

        if "/" in date:
            month, day, year = map(int, date.split("/"))

            if 0 < month <= 12 and 0 < day <=31 and year > 0:
                break
            else:
                continue
        elif "," in date:
            month, day, year = date.split()
            day = day.replace(",", "")
            month = months.index(month) + 1
            month, day, year = map(int, [month, day, year])

            if 0 < month <= 12 and 0 < day <=31 and year > 0:
                break
            else:
                continue
    except ValueError:
        continue

print(f"{year:02}-{month:02}-{day:02}")