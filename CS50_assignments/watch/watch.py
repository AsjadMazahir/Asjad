import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if not s.startswith("<iframe") or not s.endswith("</iframe>"):
        return None
    match = re.search(r"(https?://)(?:www\.)?(youtube)\.com/embed(/\w+)", s)
    if match:
        x = match.group(1).replace('http:', 'https:')
        y = match.group(2).replace('youtube', 'youtu.be')
        z = match.group(3)
        link = x + y + z
        return link
    else:
        return None

...


if __name__ == "__main__":
    main()
