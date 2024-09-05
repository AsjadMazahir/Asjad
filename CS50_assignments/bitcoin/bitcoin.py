import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Missing Command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many arguments")

try:
    coins = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    obj = response.json()
    #print(json.dumps(obj, indent=2))
    rate = obj["bpi"]["USD"]["rate_float"]
    total_cost = rate * coins
    print(f"${total_cost:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("Error while processing request")
