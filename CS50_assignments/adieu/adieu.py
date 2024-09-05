import inflect

p = inflect.engine()

mylist = []

while True:
    try:
        item = input()
        mylist.append(item)

    except EOFError:
        mymsg = p.join(mylist)
        print("Adieu, adieu, to " + mymsg)
        break
