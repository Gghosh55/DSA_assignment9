def isPowerOfTwo(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    elif n % 2 != 0:
        return False
    else:
        return isPowerOfTwo(n // 2)
print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
