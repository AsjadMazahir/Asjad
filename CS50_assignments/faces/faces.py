"""This program converts :) and :( to emoji """

def convert(word):
    word = word.replace(":)", "🙂")
    return word.replace(":(", "🙁")

def main():
    word = input("Say something: ")
    print(convert(word))

if __name__ == "__main__":
    main()