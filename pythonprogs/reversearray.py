a = [1,2,3,4,5]
b = []
# First Method
index = len(a)

while index > 0:
    b.append(a[index-1])
    index = index - 1
print(b)


#""" Second method
start = 0
end = len(a) - 1
while start < end:
    a[start],a[end] = a[end],a[start]
    start += 1
    end -= 1
print(a)


#"""