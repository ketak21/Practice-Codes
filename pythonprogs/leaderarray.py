a = [16,17,3,2,5,2]

for i in range(0,5):
    for b in range(i+1,5):
        if a[i] <= a[b]:
            break
    else:
        print(a[i])
