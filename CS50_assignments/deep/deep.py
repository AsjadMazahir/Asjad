# Prompting the user
answer = input("What is the Answer to Great Question of Life, the Universe and Everything? ").lower().strip()

if answer == '42' or answer == 'forty two' or answer == 'forty-two':
    print("Yes")
else:
    print("No")