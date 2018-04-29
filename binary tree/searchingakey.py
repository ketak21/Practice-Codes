class Node:
    def __init__(self,key):
        self.data = key
        self.right = None
        self.left = None

def search(r,value):
    if r is None:
        return 0
    if r.data == value:
        return r
    if r.data < value:
        return search(r.left,value)
        print(r.left.data)
    return search(r.right,value)

root = Node(6)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(7)
root.right.left = Node(5)
p = search(root,5)
print(p)


