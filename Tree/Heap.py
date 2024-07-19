class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

    def peek_of_heap(self, rootNode):
        if not rootNode:
            return
        return rootNode.custom_list[1]

    def size_of_heap(self, rootNode):
        if not rootNode:
            return 0
        return rootNode.heapSize

    def level_order_traversal(self, rootNode):
        data = []
        if not rootNode:
            return
        else:
            for i in range(1, rootNode.heapSize + 1):
                data.append(rootNode.custom_list[i])
        print(data)

    def heapifyTreeInsert(self, rootNode, index, heapType):
        parent_index = int(index / 2)  # because 2n/2 will give same as 2n+1/2
        if index <= 1:
            return

        if heapType == "Min":
            if rootNode.custom_list[index] < rootNode.custom_list[parent_index]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[parent_index]
                rootNode.custom_list[parent_index] = temp
            self.heapifyTreeInsert(rootNode, parent_index, heapType)

        if heapType == "Max":
            if rootNode.custom_list[index] > rootNode.custom_list[parent_index]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[parent_index]
                rootNode.custom_list[parent_index] = temp
            self.heapifyTreeInsert(rootNode, parent_index, heapType)

    def child(self, parentNode, index, type):
        left_child_index = 2 * index
        right_child_index = left_child_index + 1

        if type == "Max":
            if parentNode.custom_list[left_child_index] > parentNode.custom_list[right_child_index]:
                return left_child_index
            else:
                return right_child_index
        elif type == "Min":
            if parentNode.custom_list[left_child_index] > parentNode.custom_list[right_child_index]:
                return right_child_index
            else:
                return left_child_index

    def heapifyTreeExtract(self, rootNode, index, heapType):
        if index*2 >= rootNode.heapSize:
            return

        child = self.child(rootNode, index, heapType)
        if heapType == "Max":
            if rootNode.custom_list[index] < rootNode.custom_list[child]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[child]
                rootNode.custom_list[child] = temp
                self.heapifyTreeInsert(rootNode, child, heapType)
            return

        if heapType == "Min":
            if rootNode.custom_list[index] > rootNode.custom_list[child]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[child]
                rootNode.custom_list[child] = temp
                self.heapifyTreeInsert(rootNode, child, heapType)
            return
    def insert_node(self, rootNode, value, heapType):
        if rootNode.heapSize + 1 == rootNode.maxSize:
            return "Heap is full"
        rootNode.custom_list[rootNode.heapSize + 1] = value
        rootNode.heapSize += 1
        self.heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
        return ("value added")

    def extract_node(self, rootNode, heapType):
        # swap last index to root and remove last index, set heap size to -1 too
        rootNode.custom_list[1] = rootNode.custom_list[rootNode.heapSize]
        rootNode.custom_list[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        self.heapifyTreeExtract(rootNode, 1, heapType)


if __name__ == "__main__":
    heap = Heap(5)
    heapType = "Min"
    heap.insert_node(heap, 4, heapType)
    heap.insert_node(heap, 5, heapType)
    heap.insert_node(heap, 2, heapType)
    heap.insert_node(heap, 1, heapType)
    heap.extract_node(heap, heapType)
    heap.extract_node(heap, heapType)
    heap.level_order_traversal(heap)
