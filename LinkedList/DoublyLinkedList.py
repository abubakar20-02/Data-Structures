class Node:
    def __init__(self):
        self.prev = None
        self.next = None
        self.value = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_item(self, value):
        node = Node()
        node.value = value
        if self.head == self.tail is None:
            node.next = None
            node.prev = None

            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

    def list_item_ascending(self):
        result = []
        node = self.head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result

    def list_item_descending(self):
        result = []
        node = self.tail
        while node is not None:
            result.append(node.value)
            node = node.prev
        return result

    def pop_item(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None

        self.tail = self.tail.prev
        self.tail.next = None

    def remove_item(self, value):
        # if empty list, return
        if self.head is None:
            return

        node = self.head

        # traverse through list
        while node is not None:
            if node.value == value:

                # set prev node and next node
                prev_node = node.prev
                next_node = node.next

                if prev_node is None:
                    # Node is the head
                    self.head = next_node
                    if next_node is not None:
                        next_node.prev = None
                    else:
                        # List is now empty
                        self.tail = None
                elif next_node is None:
                    # Node is the tail
                    self.tail = prev_node
                    prev_node.next = None
                else:
                    # Node is in the middle
                    prev_node.next = next_node
                    next_node.prev = prev_node

            node = node.next


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.add_item(10)
    doubly_linked_list.add_item(20)
    doubly_linked_list.add_item(30)
    doubly_linked_list.add_item(40)
    doubly_linked_list.add_item(30)
    doubly_linked_list.remove_item(30)

    print(doubly_linked_list.list_item_ascending())
