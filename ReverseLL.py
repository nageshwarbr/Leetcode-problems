class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def reverse(self):
        head_ptr = self.head
        helper_ptr = Node(None)
        while head_ptr is not None:
            next = head_ptr.next
            head_ptr.next = helper_ptr
            helper_ptr = head_ptr
            head_ptr = next
        self.head=helper_ptr

    def printList(self):  # print all elements
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += str(temp.data) + " "
            temp = temp.next
        print(linked_list)


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(5)
LL2.insert(7)
LL2.printList()
LL2.reverse()
LL2.printList()
