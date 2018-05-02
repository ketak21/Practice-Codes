def create():
    stack = []
    return stack
def push(stack,x):
    stack.append(x)
def isEmpty(stack):
    return len(stack) == 0
def pop(stack):
    if not isEmpty(stack):
        return stack.pop()
    else:
        print("Underflow")

def next(arr):
    s = create()
    next = 0
    element = 0

    push(s,arr[0])
    for i in range(1,len(arr),1):
        next = arr[i]
        if not isEmpty(s):
            element = pop(s)
        while element < next:
            print(str(element) + "----" + str(next))
            if isEmpty(s):
                break
            element = pop(s)

        if element > next:
            push(s,element)
        push(s,next)


arr = [5,1,6,5,4,9]
next(arr)

