class Node:
    def __init__(self):
        self.value = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Length = None

    def add_item(self, value):

        # Initialize new node
        node = Node()

        # add value to new node and set the next node to be null
        node.value = value
        node.next = None

        # check if the list exists, and if it does not then initialize the list to start
        # with first element and head and tail pointing to it.
        if self.Head is None:
            self.Head = self.Tail = node
            self.Length = 1
        else:
            # if list exist then set previous node to point to the new node instead of null
            self.Tail.next = node
            self.Tail = node
            self.Length += 1

    def pop_item(self):
        node = self.Head

        # if the linked list is empty, don't do anything
        if node is None:
            return

        if self.Head == self.Tail:
            # The list has only one node
            self.Head = self.Tail = None

        # Find the position of the node before the tail
        while node.next != self.Tail:
            node = node.next

        node.next = None
        self.Tail = node
        self.Length -= 1

    def remove_item(self, value):
        node = self.Head
        prev_node = self.Head

        if node is None:
            return

        while node is not None:
            if node.value == value:
                prev_node.next = node.next
                self.Length -= 1
            prev_node = node
            node = node.next

    def len(self):
        return self.Length

    def list_item(self):
        items = []
        node = self.Head
        while node is not None:
            items.append(node.value)
            node = node.next
        return items


if __name__ == "__main__":
    LinkedList = LinkedList()

    LinkedList.add_item(10)
    LinkedList.add_item(20)
    LinkedList.add_item(30)
    LinkedList.add_item(20)
    LinkedList.remove_item(20)

    print(LinkedList.list_item())
    print(LinkedList.len())
