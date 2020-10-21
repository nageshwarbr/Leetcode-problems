class LinkedList:
    def __init__(self):
        self.head = None

    def removeNthFromLast(self, n):
        ans = Node(None)
        ans.next = self.head
        first = ans
        second = ans

        for i in range(i, n + 2):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return ans.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
