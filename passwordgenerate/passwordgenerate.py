import random

class PasswordGenerate():
    # Variables Characters
    lowerchars = "abcdefghijklmnopqrstuvwxyz"
    upperchars = lowerchars.upper()
    numberschars = "0123456789"
    specialchars = "{}[],.;-_+="

    # Group Variables
    allchars = lowerchars + upperchars + numberschars + specialchars
    # Total length of password
    length = int(input("Type total lenght the password: "))

    # Result password
    password = "".join(random.sample(allchars, length))
    print(password)

    pass
