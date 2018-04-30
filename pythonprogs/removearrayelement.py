a = [10,20,20,30,30,40,50]
b = len(a)
key = 20
i = 0
c = len(a)
while i < c:
    if a[i]!=key:
        i = i + 1
    else:
        a.pop(i)
        next(i)



print(a)