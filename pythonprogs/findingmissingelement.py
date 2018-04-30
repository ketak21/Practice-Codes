#Finding Missing Element
"""a = [1,2,3,5,6,9,8,7]
def missingelement(arr):
    n = len(arr)
    total = (n+1)*(n+2)/2
    sumofarr = sum(arr)
    return total-sumofarr

p = missingelement(a)
print (p)"""

#2nd Method using XOR which is better because if the array is big then the sum of array becomes very big to store
#Time complexity of both methods is O(n)
arr = [1,2,3,6,5,7,8]
def missingelement(a):
    n = len(a)
    X1 = 0
    X2 = 0
    for i in range(n):
        X1 ^= a[i]
    for i in range(n+2):
         X1 ^= i
    return X1^X2

p = missingelement(arr)
print(p)
