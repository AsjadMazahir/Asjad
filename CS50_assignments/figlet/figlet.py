from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 2 or len(sys.argv) > 3:
    print("here")
    sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    my_text = input("Enter the text:")
    my_font = random.choice(figlet.getFonts())

elif (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
    my_text = input("Enter the text:")
    my_font = sys.argv[2]

else:
    sys.exit("Invalid usage")

figlet.setFont(font = my_font)
print(figlet.renderText(my_text))