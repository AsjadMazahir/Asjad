word = input("Say something: ")
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for c in word:
    if c in vowels:
        word = word.replace(c, "")

print(word)