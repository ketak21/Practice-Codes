

def onebit(b):
    c = 0
    while c < len(b):
        if c == len(b) - 1:
            return True
        if b[c] == 0:
            c = c +1
        else:
            c = c + 2
            return False

b = [0,1,0,1,0]
print(onebit(b))

