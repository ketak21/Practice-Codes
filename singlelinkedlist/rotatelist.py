class Node:
    def __init__(self,data):
        self .data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
    def rotate(self,k):
        if k == 0:
            return
        current = self.head
        count = 1
        while(count<k and current is not None):
            current = current.next
            count += 1
        if current is None:
            return
        kthnode = current
        while(current.next is not None):
            current = current.next
        current.next = self.head
        self.head = kthnode.next
        kthnode.next = None

llist = LinkedList()

# Create a list 10->20->30->40->50->60
for i in range(60, 0, -10):
    llist.push(i)

print ("Given linked list")
llist.print()
llist.rotate(4)

print("\nRotated Linked list")
llist.print()






