#Search operation in an array

arr = [10,20,30,40,50]
key = 40
def search(a,key):
    for i in range(len(a)):
        if arr[i] == key:
            return i
    return -1


index = search(arr,key)
if index != -1:
    print("Element found at: " + str(index + 1))
else:
    print("Element not found")