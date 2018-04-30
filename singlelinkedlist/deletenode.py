class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def deletenode(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None
    def print(self):
        temp = self.head
        while (temp):
            print ("%d" %(temp.data),end=" ")
            temp = temp.next

if __name__ == '__main__':
    list = LinkedList()
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
    list.append(7)
    print("Created LinkedList:")
    list.print()
    list.deletenode(5)
    print("\nLinkedList after deletion")
    list.print()

