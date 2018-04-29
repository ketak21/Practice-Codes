class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def preorder(root):
    if root:
       preorder(root.left)
       print(root.val)
       preorder(root.right)

def inorder(root):
    if root:
        print(root.val)
        inorder(root.left)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(4)
print("Preorder Traversal")
preorder(root)
print("Inorder Traversal")
inorder(root)
print("Postorder Traversal")
postorder(root)
