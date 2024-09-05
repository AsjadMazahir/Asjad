import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

content=[]
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if not line.lstrip().startswith("#") and not line == "\n" and not line.isspace():
                content.append(line)
        print(len(content))

except FileNotFoundError:
    sys.exit("File does not exist")