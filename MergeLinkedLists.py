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

    def printList(self):  # print all elements
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += str(temp.data) + " "
            temp = temp.next
        print(linked_list)


def merge(List1, List2):
    head_ptr = temp_ptr = Node(None)
    while List1 or List2:
        if List1 and (not List2 or List1.data <= List2.data):
            temp_ptr.next = Node(List1.data)
            List1 = List1.next
        else:
            temp_ptr.next = Node(List2.data)
            List2 = List2.next

        temp_ptr = temp_ptr.next
    return head_ptr.next


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List with even numbers
LL1 = LinkedList()
LL1.insert(2)
LL1.insert(4)
LL1.insert(6)
LL1.insert(8)
# Linked List with odd numbers
LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(5)
LL2.insert(7)
# Merge Function
LL3 = LinkedList()
LL3.head = merge(LL1.head, LL2.head)
LL3.printList()
