input = [-1, 0, 1, 2, -1, -4]
def sumthree(a):
    s = set()
    temp = 0
    for i in range (len(a)-1):
        temp = - a[i] - a[i+1]
        if temp in s:
            print (str(temp) +" " + str(a[i]) +" " + str(a[i+1]))
        s.add(a[i])
        s.add(a[i+1])

sumthree(input)


