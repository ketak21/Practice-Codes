#Max Sum of non adjacent numbers
def maxsum(arr):
    incl = 0
    excl =0
    for i in arr:
        newexcl = max(incl,excl)
        incl = excl + i
        excl = newexcl
    return max(incl,excl)

a = [5,5,10,100,10,5]
p = maxsum(a)
print(p)