class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        current = self.root
        for char in word:
            # if char is not in dict
            if char not in current.children:
                # create dict for that letter
                current.children[char] = TrieNode()
            # traverse to different letter dict
            current = current.children[char]
        # set last node to be end of word
        current.end_of_word = True

    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.end_of_word


def deleteString(root, word, index):
    if index == len(word):
        # We've reached the end of the word.
        if root.end_of_word:
            root.end_of_word = False
            # If this node has no children, it can be deleted.
            return len(root.children) == 0
        return False

    char = word[index]
    currentNode = root.children.get(char)
    if not currentNode:
        return False

    canDeleteCurrentNode = deleteString(currentNode, word, index + 1)

    if canDeleteCurrentNode:
        del root.children[char]
        # Return True if no children are left in the root node and it's not end of another word.
        return len(root.children) == 0 and not root.end_of_word

    return False


if __name__ == "__main__":
    trie = Trie()
    trie.add_word("abu")
    trie.add_word("abdul")
    # trie.add_word("abdullah")
    deleteString(trie.root, "f", 0)
    print(trie.exists("abdul"))
