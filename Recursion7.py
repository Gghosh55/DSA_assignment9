from itertools import permutations

def generatePermutations(S):
    perm_set = set(permutations(S))
    result = [''.join(perm) for perm in perm_set]
    return result
S1 = "ABC"
print(generatePermutations(S1))  # Output: ['CAB', 'ACB', 'BCA', 'BAC', 'CBA', 'ABC']

S2 = "XY"
print(generatePermutations(S2))  # Output: ['YX', 'XY']
