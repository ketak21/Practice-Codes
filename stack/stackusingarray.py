from sys import maxsize
def create():
    stack = []
    return stack
def isempty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)
    print("Pushed to stack " + item)

def pop(stack):
    if isempty(stack):
        return str(-maxsize-1)
    return stack.pop()
stack = create()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")