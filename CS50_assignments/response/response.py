import validators

s = input("What's your email address? ")

if validators.email(s) == True:
    print("Valid")
else:
    print("Invalid")