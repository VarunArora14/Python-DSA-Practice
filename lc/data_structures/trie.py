class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]

        node.is_end_of_word = True

    def __search_helper(self, word: str):
        node = self.root
        for w in word:
            if w not in node.children:
                return None
            node = node.children[w]

        return node

    def search(self, word: str):
        res = self.__search_helper(word)
        if res is None or not res.is_end_of_word:
            return False
        return True

    def starts_with(self, prefix: str):
        res = self.__search_helper(word=prefix)
        return res is not None
