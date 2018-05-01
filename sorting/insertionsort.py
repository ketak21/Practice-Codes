def insertion(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
arr = [23,6,3,4,5,1,0]
insertion(arr)
for i in range(len(arr)):
    print(arr[i])
