import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

table = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        print(tabulate(table, headers = "firstrow", tablefmt = "grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
