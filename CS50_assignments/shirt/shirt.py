import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].lower().endswith((".jpg", ".jpeg", "png")) or not sys.argv[2].lower().endswith((".jpg", ".jpeg", "png")):
    sys.exit("Invalid input")

file1_ext = os.path.splitext(sys.argv[1])[1]
file2_ext = os.path.splitext(sys.argv[2])[1]

if file1_ext != file2_ext:
    sys.exit("Input and output have different extensions")

#opening the images
shirt = Image.open("shirt.png")
try:
    muppet = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exit")

#taking shirt size
size = shirt.size

#cropping the before image
new_muppet = ImageOps.fit(muppet, size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5,0.5))

#pasting
new_muppet.paste(shirt, shirt)

#saving
new_muppet.save(sys.argv[2])