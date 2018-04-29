class Node:
    def __init__(self,key):
        self.data = key
        self.right = None
        self.left = None

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)

        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

def minimum(root):
    if root is None:
        return 0
    while(root.left is not None):
        root = root.left
    return root.data


def printorder(root):
    if root:
        printorder(root.left)
        print(root.data)
        printorder(root.right)


r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
printorder(r)
print("Minimum value in the tree is ",minimum(r))
