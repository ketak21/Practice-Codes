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
    def deleteposition(self,position):
        temp = self.head
        if self.head == None:
            return
        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
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
    list.deleteposition(3)
    print("\nLinkedList after deletion")
    list.print()