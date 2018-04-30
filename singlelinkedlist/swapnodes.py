class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList(object):
    def __init__(self):
        self.head = None
    def swapnodes(self,x,y):
        if x == y:
            return
        prevx = None
        currx = self.head
        while currx != None and currx.data != x:
            prevx = currx
            currx = currx.next
        prevy = None
        curry = self.head
        while curry != None and curry.data != y:
            prevy = curry
            curry = curry.next
        if currx == None or curry == None:
            return
        if prevx != None:
            prevx.next = curry
        else:
            self.head = curry
        if prevy != None:
            prevy.next = currx
        else:
            self.head = currx
        temp = currx.next
        currx.next = curry.next
        curry.next = temp

    def append(self,data):
        new_node = Node(data)
        print(new_node)
        new_node.next = self.head
        self.head = new_node
        print(self.head)
    def print(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
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
    list.swapnodes(4,6)
    print("\nNew List")
    list.print()

