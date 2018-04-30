#Rotating Array by a some number
def numberofrotation(arr,d,n):
    for i in range(d):
        rotatearray(arr,n)
        print(arr)

def rotatearray(arr,n):
    temp = arr[0]
    for i in range(0,n-1):
        arr[i] = arr[i+1]
    arr[i+1] = temp

a = [1,2,3,4,5,6]
n = len(a)
numberofrotation(a,2,n)
