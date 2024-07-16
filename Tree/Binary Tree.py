class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value


class Tree:
    def __init__(self, root_value):

        self.root = Node(root_value)

    def __insert_item__(self, root, value):
        if value > root.value:
            if root.right_child is None:
                root.right_child = Node(value)
                print("Inserted in right child")
            else:
                self.__insert_item__(root.right_child, value)
        else:
            if root.left_child is None:
                root.left_child = Node(value)
                print("Inserted in left child")
            else:
                self.__insert_item__(root.left_child, value)

    def insert_item(self, value):
        self.__insert_item__(self.root, value)

    def find_item(self, value):
        return self.__find_item__(self.root, value)

    def preorder_traversal(self):
        data = []
        self.__preorder_traversal__(self.root, data)
        return data

    def inorder_traversal(self):
        data = []
        self.__inorder_traversal__(self.root, data)
        return data

    def postorder_traversal(self):
        data = []
        self.__inorder_traversal__(self.root, data)
        return data

    def delete(self, value):
        self.__deleteNode__(self.root, value)

    def __find_item__(self, root, value):
        if root.value == value:
            return True
        if root.value < value:
            if root.right_child is None:
                return False
            else:
                return self.__find_item__(root.right_child, value)
        else:
            if root.left_child is None:
                return False
            else:
                return self.__find_item__(root.left_child, value)

    def __preorder_traversal__(self, root, data):
        if root is None:
            return
        data.append(root.value)
        self.__preorder_traversal__(root.left_child, data)
        self.__preorder_traversal__(root.right_child, data)

    def __postorder_traversal__(self, root, data):
        if root is None:
            return
        self.__postorder_traversal__(root.left_child, data)
        self.__postorder_traversal__(root.right_child, data)
        data.append(root.value)

    def __inorder_traversal__(self, root, data):
        if root is None:
            return
        self.__inorder_traversal__(root.left_child, data)
        data.append(root.value)
        self.__inorder_traversal__(root.right_child, data)

    def minValueNode(self, bstNode):
        current = bstNode
        while current.left_child is not None:
            current = current.left_child
        return current

    def __deleteNode__(self, root, value):
        if root is None:
            return None  # Base case: if the tree is empty, return None
        elif value < root.value:
            # If the value to be deleted is smaller than the root's value,
            # then it lies in the left subtree
            root.left_child = self.__deleteNode__(root.left_child, value)
        elif value > root.value:
            # If the value to be deleted is greater than the root's value,
            # then it lies in the right subtree
            root.right_child = self.__deleteNode__(root.right_child, value)
        else:
            # If the value is the same as the root's value, then this is the node
            # to be deleted
            if root.left_child is None:
                # Node with only right child or no child
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                # Node with only left child
                temp = root.left_child
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = self.minValueNode(root.right_child)
            # Copy the inorder successor's value to this node
            root.value = temp.value
            # Delete the inorder successor
            root.right_child = self.__deleteNode__(root.right_child, temp.value)
        return root


if __name__ == "__main__":
    bst = Tree(10)
    bst.insert_item(11)
    bst.insert_item(9)
    bst.insert_item(10)
    bst.delete(11)

    print(bst.inorder_traversal())
