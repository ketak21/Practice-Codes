
def odd(arr):
    res = 0
    for i in arr:
        res = res ^ i

    return res

a = [1,2,3,2,3,4,1,5,5]
p = odd(a)
print(p)
"""def getOddOccurrence(arr):

    # Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element

    return res

# Test array
arr = [1,2,2,3,3]

print ("%d" % getOddOccurrence(arr))"""

