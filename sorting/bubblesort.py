def bubblesort(a):
    for i in range(len(a)):
        n = len(a)
        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

arr = [20,7,2,15,7,50]
bubblesort(arr)
for i in range(len(arr)):
    print(arr[i])