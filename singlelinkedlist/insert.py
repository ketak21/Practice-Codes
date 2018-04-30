class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#Insert at the start

    def push(self,data):
        new_node = Node(data)
        print(new_node)
        new_node.next = self.head
        self.head = new_node
        print(self.head)

#Insert after something
    def insertafter(self,prev_node,data):
        if prev_node is None:
            print("Not in linked list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    def print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    list = LinkedList()
    list.push(8)

    third = Node(11)
    list.head.next = third
    list.append(9)
    list.insertafter(third.next,10)
    list.print()







