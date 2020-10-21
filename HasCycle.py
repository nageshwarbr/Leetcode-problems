class LinkedList(object):
    def __init__(self):
        self.head = None

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                return True
        return False


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(5)
LL2.insert(7)

