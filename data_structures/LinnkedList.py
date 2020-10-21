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

    def insert_at_pos(self, item, index):
        current = self.head
        counter = 0
        Temp = Node(item)

        Prev = None

        if index == 0:
            self.head = Temp.next
            self.head = Temp
        else:
            while counter < index:
                Prev = current
                current = current.next
                counter = counter + 1

            Temp.next = current
            Prev.next = Temp

    def delete_node(self, key):
        del_nde = Node(key)
        current = self.head
        prev = None
        if del_nde.data == self.head.data:
            self.head = self.head.next
            return

        try:
            while current.data != del_nde.data:
                prev = current
                current = current.next

            prev.next = current.next
            current = None
        except Exception:
            print("the element does not exist")


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


l_list = LinkedList()
l_list.head = Node(5)
second = Node(1)
third = Node(3)
fourth = Node(7)

l_list.head.next = second
second.next = third
third.next = fourth

l_list.printList()
# l_list.insert_at_pos(3, 4)
l_list.delete_node(5)
l_list.printList()
