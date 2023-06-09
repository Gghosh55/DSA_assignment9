def productOfArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product
arr1 = [1, 2, 3, 4, 5]
print(productOfArray(arr1))

arr2 = [1, 6, 3]
print(productOfArray(arr2))
