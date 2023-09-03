arrStr = input()
arr = arrStr.split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

target = int(input())

flag = False
for i in arr:
    res = target - i
    if res in arr:
        flag = True
        print(f'yes, {target} = {i} + {res}')
        break

if not flag:    print("no")