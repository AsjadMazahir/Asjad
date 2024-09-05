def main():
    w = input("Say something: ")
    print(shorten(w))

def shorten(word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for c in word:
        if c in vowels:
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()