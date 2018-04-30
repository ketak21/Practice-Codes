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
    def sumoflists(self,first,second):
        prev = None
        temp = None
        carry = 0
        while(first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            sum = fdata + sdata + carry

            if sum >= 10:
                carry = 1
            else:
                carry = 0
            sum = sum if sum < 10 else sum % 10
            temp = Node(sum)
            print("\n"+ str(sum))
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)

first = LinkedList()
second = LinkedList()

# Create first list
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
print ("First List is ")
first.print()

# Create second list
second.push(4)
second.push(8)
print ("\nSecond List is ")
second.print()

# Add the two lists and see result
res = LinkedList()
res.sumoflists(first.head, second.head)
print ("\nResultant")
res.print()