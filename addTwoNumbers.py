class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):  # print all elements
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += str(temp.data) + " "
            temp = temp.next
        print(linked_list)

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def addTwoNumbers(list1, list2):
    l1 = list1.head
    l2 = list2.head
    # ans = Node(None)
    # pointer = ans
    head_ptr = pointer = Node(None)

    carry = 0

    while l1 is not None or l2 is not None:
        sum = carry
        if l1 is not None:
            sum += l1.data
            l1 = l1.next
        if l2 is not None:
            sum += l2.data
            l2 = l2.next

        carry = int(sum / 10)
        pointer.next = Node(sum % 10)

        pointer = pointer.next

    if carry > 0:
        pointer.next = Node(carry)

    return head_ptr.next


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
LL3 = LinkedList()
LL3.head = addTwoNumbers(LL1, LL2)
LL3.printList()
