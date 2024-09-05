import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.match(r"^((?:[1][0-2])|(?:[1-9])):?(?:[0-5][0-9])? (AM|PM) to ((?:[1][0-2])|(?:[1-9])):?(?:[0-5][0-9])? (AM|PM)$", s.strip())
    if match:
        if match.group(2) == "PM":
            x = f"{int(match.group(1)) + 12:02}"
            if int(match.group(1) == 12):
                x = f"{int(match.group(1)):02}"
        else:
            x = f"{int(match.group(1)):02}"
            if int(match.group(1)) == 12:
                x = f"{int(match.group(1)) - 12:02}"
        if match.group(4) == "PM":
            y = f"{int(match.group(3)) + 12:02}"
            if int(match.group(3)) == 12:
                y = f"{int(match.group(3)):02}"
        else:
            y = f"{int(match.group(3)):02}"
            if int(match.group(3)) == 12:
                y = f"{int(match.group(3)) - 12:02}"

        new_match = re.sub(" AM|PM", "", match.group())
        my_list =  new_match.split()
        if ":" in my_list[0]:
            hr_start, min_start = x, my_list[0].split(":")[1]
        else:
            hr_start, min_start = x, "00"
        if ":" in my_list[2]:
            hr_end, min_end = y, my_list[2].split(":")[1]
        else:
            hr_end, min_end = y, "00"

        converted_text = f"{hr_start}:{min_start} to {hr_end}:{min_end}"
        return converted_text

    else:
        raise ValueError

if __name__ == "__main__":
    main()