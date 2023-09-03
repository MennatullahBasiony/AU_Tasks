def binSearch(target, l, r, arr):

    midIndex = (l + r) // 2
    mid = arr[midIndex]
    if mid < target:
        return binSearch(target, midIndex+1, r, arr)
    elif mid > target:
        return binSearch(target, l, midIndex-1, arr)
    else:
        return midIndex

arr = [3, 5, 6, 7, 8, 9]
print(binSearch(8, 0, 5, arr))