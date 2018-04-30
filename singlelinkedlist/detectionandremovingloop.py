class Node:
    def __init__(self,data):
        self.data = data
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
            print(temp.data,end=" ")
            temp = temp.next

    def detectloop(self):
        slow = self.head
        fast = self.head
        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("\nLoop found")
                self.remove(slow)
                return
    def remove(self,loopnode):
        pt1 = self.head
        while (1):
            pt2 = loopnode
            while (pt2.next != loopnode and pt2.next != pt1):
                pt2 = pt2.next
            if pt2.next == pt1:
                print("head")
                break
            pt1 = pt1.next

        pt2.next = None

if __name__ == '__main__':
    lst = LinkedList()
    lst.push(10)
    lst.push(20)
    lst.push(30)
    lst.push(40)
    print("Created list")
    lst.print()

    lst.head.next.next.next.next = lst.head
    lst.detectloop()
    print("LinkedList after removing loop")
    lst.print()