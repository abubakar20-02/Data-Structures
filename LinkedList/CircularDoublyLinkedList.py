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
        if self.head is None:
            node.next = node.prev = node
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
            self.tail = node

    def list_item_ascending(self):
        result = []
        if self.head is None:
            return result
        node = self.head
        while True:
            result.append(node.value)
            node = node.next
            if node == self.head:
                break
        return result

    def list_item_descending(self):
        result = []
        if self.tail is None:
            return result
        node = self.tail
        while True:
            result.append(node.value)
            node = node.prev
            if node == self.tail:
                break
        return result

    def pop_item(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    def remove_item(self, value):
        if self.head is None:
            return

        node = self.head
        while True:
            if node.value == value:
                prev_node = node.prev
                next_node = node.next

                if prev_node == next_node == node:
                    self.head = self.tail = None
                else:
                    if node == self.head:
                        self.head = next_node
                        self.tail.next = self.head
                        self.head.prev = self.tail
                    elif node == self.tail:
                        self.tail = prev_node
                        self.tail.next = self.head
                        self.head.prev = self.tail
                    else:
                        prev_node.next = next_node
                        next_node.prev = prev_node

                if self.head is None:
                    break

                if node == self.tail:
                    break

            node = node.next
            if node == self.head:
                break


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.add_item(10)
    doubly_linked_list.add_item(20)
    doubly_linked_list.add_item(30)
    doubly_linked_list.add_item(40)
    doubly_linked_list.add_item(30)
    doubly_linked_list.remove_item(30)

    print(doubly_linked_list.list_item_ascending())
