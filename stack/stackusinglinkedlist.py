from sys import maxsize
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
    def isEmpty(self):
        return True if self.root is None else False

    def pop(self):
        if self.isEmpty():
            return str(-maxsize -1)
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if (self.isEmpty()):
            return str(-maxsize -1)
        return self.root.data
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print ("%s popped from stack" %(stack.pop()))
print ("Top element is %s " %(stack.peek()))


