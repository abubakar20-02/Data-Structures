class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None

    def __pre_order_traversal__(self, root, data):
        if root is None:
            return None
        data.append(root.value)
        self.__pre_order_traversal__(root.left_child, data)
        self.__pre_order_traversal__(root.right_child, data)

    def __post_order_traversal__(self, root, data):
        if root is None:
            return None
        self.__post_order_traversal__(root.left_child, data)
        self.__post_order_traversal__(root.right_child, data)
        data.append(root.value)

    def __in_order_traversal__(self, root, data):
        if root is None:
            return None
        self.__in_order_traversal__(root.left_child, data)
        data.append(root.value)
        self.__in_order_traversal__(root.right_child, data)

    def pre_order_traversal(self):
        data = []
        self.__pre_order_traversal__(self.root, data)
        return data

    def post_order_traversal(self):
        data = []
        self.__post_order_traversal__(self.root, data)
        return data

    def in_order_traversal(self):
        data = []
        self.__in_order_traversal__(self.root, data)
        return data

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def rotate_right(self, imbalanced_node):
        new_root = imbalanced_node.left_child  # The child of root becomes the new root
        imbalanced_node.left_child = new_root.right_child  # The grandchild becomes the child
        new_root.right_child = imbalanced_node  # The old root becomes child

        # Recalculate height of the new root and old root
        imbalanced_node.height = 1 + max(self.get_height(imbalanced_node.left_child),
                                         self.get_height(imbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))

        return new_root

    def rotate_left(self, imbalanced_node):
        new_root = imbalanced_node.right_child  # The child of root becomes the new root
        imbalanced_node.right_child = new_root.left_child  # The grandchild becomes the child
        new_root.left_child = imbalanced_node  # The old root becomes child

        # Recalculate height of the new root and old root
        imbalanced_node.height = 1 + max(self.get_height(imbalanced_node.left_child),
                                         self.get_height(imbalanced_node.right_child))
        new_root.height = 1 + max(self.get_height(new_root.left_child), self.get_height(new_root.right_child))

        return new_root

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left_child) - self.get_height(root.right_child)

    def insert_item(self, value):
        self.root = self.__insert_item__(self.root, value)

    def delete_item(self, value):
        self.root = self.__delete_item__(self.root, value)

    def __insert_item__(self, root, value):
        if root is None:
            return Node(value)

        if root.value > value:
            root.left_child = self.__insert_item__(root.left_child, value)
        else:
            root.right_child = self.__insert_item__(root.right_child, value)

        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))

        balance = self.get_balance(root)

        # more on left side
        # LL
        if balance > 1:
            if value < root.left_child.value:
                return self.rotate_right(root)
            else:
                # LR
                root.left_child = self.rotate_left(root.left_child)
                return self.rotate_right(root)
        if balance < -1:
            # RR
            if value > root.right_child.value:
                return self.rotate_left(root)
            else:
                # RL
                root.right_child = self.rotate_right(root.right_child)
                return self.rotate_left(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left_child is None:
            return root
        return self.get_min_value_node(root.left_child)

    def __delete_item__(self, root, value):
        if root is None:
            return root

        if value > root.value:
            root.right_child = self.__delete_item__(root.right_child, value)
        elif value < root.value:
            root.left_child = self.__delete_item__(root.left_child, value)
        else:
            if root.right_child is None:
                temp = root.left_child
                root = None
                return temp

            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = self.get_min_value_node(root.right_child)
            # Copy the inorder successor's value to this node
            root.value = temp.value
            # Delete the inorder successor
            root.right_child = self.__delete_item__(root.right_child, temp.value)

        balance = self.get_balance(root)
        if balance > 1:
            # L
            if self.get_balance(root.left_child) >= 0:
                # L
                return self.rotate_right(root)
            else:
                # R
                root.left_child = self.rotate_left(root.left_child)
                self.rotate_right(root)
        if balance < -1:
            # R
            if self.get_balance(root.left_child) >= 0:
                # L
                root.right_child = self.rotate_left(root.right_child)
                self.rotate_left(root)
            else:
                # R
                return self.rotate_left(root)

        return root


if __name__ == "__main__":
    avl = AVL()
    avl.insert_item(5)
    avl.insert_item(15)
    avl.insert_item(20)
    avl.insert_item(1)

    avl.delete_item(5)

    print(avl.in_order_traversal())  # Correct function name
