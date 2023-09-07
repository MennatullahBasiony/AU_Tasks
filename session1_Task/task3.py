pounds = [200, 100, 50, 20, 10, 5, 1]
nPounds = [0, 0, 0, 0, 0, 0, 0]
i = 0

while True:
    try:
        number = int(input('Enter your amount of money: '))
        assert 0 <= number
    except ValueError:
        print("Not a Number! Please enter a Number.")
    except AssertionError:
        print("Please enter amount of money 0 or more")
    else:
        break


while number > 0:
    while number - pounds[i] >= 0:
        nPounds[i] += 1
        number -= pounds[i]

    i += 1


line = ""
for i in range(len(nPounds)):
    if nPounds[i] > 0:
        line += f'{nPounds[i]}x{pounds[i]} L.E. + '

if line == "":
    print("0 pounds")
else:
    line = line[:-2]
    print(line)



