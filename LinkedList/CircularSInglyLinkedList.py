class Node:
    def __init__(self):
        self.value = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Length = 0

    def add_item(self, value):
        # Initialize new node
        node = Node()
        node.value = value

        if self.Head is None:
            # If the list is empty, initialize Head and Tail with the new node
            self.Head = self.Tail = node
            node.next = self.Head  # Point to itself to form a circular structure
        else:
            node.next = self.Head  # New node points to the current Head
            self.Tail.next = node  # Old Tail points to the new node
            self.Tail = node       # Update the Tail to the new node

        self.Length += 1

    def pop_item(self):
        if self.Head is None:
            # The list is empty
            return None

        if self.Head == self.Tail:
            # The list has only one node
            value = self.Head.value
            self.Head = self.Tail = None
            self.Length = 0
            return value

        # Find the node before the Tail
        node = self.Head
        while node.next != self.Tail:
            node = node.next

        value = self.Tail.value
        node.next = self.Head  # Update the next of the new Tail to Head
        self.Tail = node       # Update the Tail
        self.Length -= 1

        return value

    def remove_item(self, value):
        if self.Head is None:
            # The list is empty
            return False

        current = self.Head
        previous = None

        while True:
            if current.value == value:
                if previous is not None:
                    previous.next = current.next
                    if current == self.Tail:
                        self.Tail = previous
                else:
                    # Handle case where we need to remove the head
                    if self.Head == self.Tail:
                        self.Head = self.Tail = None
                    else:
                        self.Head = current.next
                        self.Tail.next = self.Head
                self.Length -= 1
                return True

            previous = current
            current = current.next

            if current == self.Head:
                break

        return False

    def len(self):
        return self.Length

    def list_item(self):
        items = []
        if self.Head is None:
            return items

        node = self.Head
        while True:
            items.append(node.value)
            node = node.next
            if node == self.Head:
                break

        return items


if __name__ == "__main__":
    linked_list = LinkedList()  # Avoid using the same name as the class

    linked_list.add_item(10)
    linked_list.add_item(20)
    linked_list.add_item(30)
    linked_list.add_item(20)
    linked_list.remove_item(20)

    print(linked_list.list_item())  # Output should reflect the removal of first occurrence of 20
    print(linked_list.len())        # Length should reflect the current number of elements
