#Largest Sum Contiguous Subarray

def largestsum(a,size):
    maxendinghere = 0
    maxsofar = 0
    for i in range(size):
        maxendinghere = maxendinghere + a[i]
        if maxendinghere < 0:
            maxendinghere = 0
        if maxendinghere > maxsofar:
            maxsofar = maxendinghere

    return maxsofar
arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
p = largestsum(arr,len(arr))

print(p)
