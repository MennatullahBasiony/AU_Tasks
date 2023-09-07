while 1:
    try:
        hight = int(input("Enter a positive integer between 1 and 8: "))
        if hight >= 1 and hight <= 8:
            break

    except ValueError:
        print("Invalid integer. The number must be in the range of 1-8.")

whiteSpaces = hight - 1
noOfLines = hight

while noOfLines > 0:
    symbol = hight - whiteSpaces
    line = " " * whiteSpaces + "#" * symbol + "  " + "#" * symbol

    print(line)
    whiteSpaces -= 1
    noOfLines -= 1
