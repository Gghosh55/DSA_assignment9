def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], findMax(arr[1:]))
arr1 = [1, 4, 3, -5, -4, 8, 6]
print(findMax(arr1))

arr2 = [1, 4, 45, 6, 10, -8]
print(findMax(arr2))
