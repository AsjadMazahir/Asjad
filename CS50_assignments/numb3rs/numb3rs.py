import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        for i in matches.groups():
            if int(i) < 0 or int(i) > 255:
                return False

        return True
    else:
        return False




if __name__ == "__main__":
    main()