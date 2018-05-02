def createstack():
    stack = []
    return stack
def size(stack):
    return len(stack)
def isEmpty(stack):
    return len(stack) == 0
def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return -1
    else:
        return stack.pop()


def reverse(string):
    n = len(string)
    stack = createstack()
    for i in range(0,n,1):
        push(stack,string[i])

    string = ""

    for i in range(0,n,1):
        string += pop(stack)

    print(string)

string = "My Name is Ankur"
reverse(string)
