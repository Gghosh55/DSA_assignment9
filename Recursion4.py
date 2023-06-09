def power(N, P):
    if P == 0:
        return 1
    else:
        return N * power(N, P - 1)
print(power(5, 2))
print(power(2, 5))
