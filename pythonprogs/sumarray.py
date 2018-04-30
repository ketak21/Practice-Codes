a =[1,2,3,4,12,11,5,4]
sum = 16
temp = 0
target = []
for i in range(0,len(a)):
    temp = sum - a[i]

    if temp > 0 and temp in a and temp not in target:
        print("the pairs are",temp,a[i])
    target.append(temp)

    target.append(a[i])
