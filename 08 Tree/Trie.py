class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True

    def searchString(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        if current.endOfString == True:
            return True
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("App"))
print(newTrie.searchString("Ap"))
print(newTrie.searchString("dcf"))
