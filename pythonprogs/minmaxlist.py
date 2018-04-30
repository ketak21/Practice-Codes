a= [5,1,2,8,0,7]

def minmax(b):
    min = b[0]
    max = b[0]
    for i in b:
        if i < min:
            min = i
        elif i > max:
            max = i

    print (min)
    print (max)

minmax(a)