def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if is_length(s):
        return False
    elif is_start_letter(s):
        return False
    elif is_punctuations(s):
        return False
    elif s.isalpha():
        return True
    elif number_validity(s):
        return False
    else:
        return True

# checking for length
def is_length(s):
    if len(s) < 2 or len(s) > 6:
        return True

# checking for starting letter
def is_start_letter(s):
    if not s[0:2].isalpha():
        return True

# checking for punctuations
def is_punctuations(s):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for c in s:
        if c in punctuations:
            return True

def number_validity(s):
        for c in s:
            if c.isdigit():
                digits = s[s.index(c):]
                break
        if digits.isdigit() and digits[0] != '0':
            return False
        else:
            return True

if __name__ == "__main__":
    main()