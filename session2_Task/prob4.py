count_open_bracket = 0
count_closed_bracket = 0


str = input("Enter your String: ")

balanced = True

for i in str:

    if i == "(":        
        count_open_bracket +=1
        
    else: 
        count_closed_bracket +=1

    if count_closed_bracket > count_open_bracket:
            balanced = False 
            break

if balanced and count_closed_bracket == count_open_bracket:
    print("Balanced")
else:
    print("Not Balanced")


