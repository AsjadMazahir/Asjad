import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit(f"Could not read {sys.argv[1]}")

data = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]
            data.append({"first": first, "last": last, "house": house})

    with open(sys.argv[2], "wr") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in data:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
except FileNotFoundError:
    sys.exit("File does not exist")