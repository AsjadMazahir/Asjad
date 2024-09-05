groc = {}

while True:
    try:
        item = input().upper()
        if item not in groc:
            groc[item] = 1
        else:
            groc[item] += 1

    except EOFError:
        break

groc_updated = dict(sorted(groc.items()))
print()
for i in groc_updated:
    print(groc_updated[i], i)

