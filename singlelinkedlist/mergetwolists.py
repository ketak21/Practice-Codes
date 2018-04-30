class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList(object):
    def __init__(self):
        self.head = None


    def print(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


def merge(l1,l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = merge(l1.next,l2)
    else:
        temp = l2
        temp.next = merge(l1,l2.next)
    return temp
if __name__ == '__main__':
    list1 = LinkedList()
    list1.push(10)
    list1.push(10)
    list1.push(10)
    list2 = LinkedList()
    list2.push(40)
    list2.push(30)
    list2.push(10)
    print("1st LinkedList")
    list1.print()
    print("2nd LinkedList")
    list2.print()
    l3 = LinkedList()
    l3.head = merge(list1.head, list2.head)
    print("Merged List")
    l3.print()