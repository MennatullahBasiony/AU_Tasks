str1 = input("Enter your first String: ")
str2 = input("Enter your second String: ")

flag = True
size = len(str1)

if size != len(str2):  print("not an anagram")

else:
    for i in range(size):
        if str1[i] != str2[size - 1 -i]:
            flag = False
            break

if flag:    print("It's an anagram")
else: print("It's not an anagram")
