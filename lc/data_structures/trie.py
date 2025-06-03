class TrieNode:
    def __init__(self, isLeaf=False):
        self.children = {}
        self.isLeaf = isLeaf


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] # go to char for next char to be added
        node.isLeaf=True
    
    def search(self,word:str) -> bool:
        if word == "":
            return True
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.isLeaf

    def contains_prefix(self, word:str) -> bool:
        if word == "":
            return True
        
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
    
t = Trie()
t.insert("hello")
t.insert("word")
print(t.contains_prefix("hell"))
print(t.contains_prefix("hello"))
print(t.contains_prefix("hellow"))
print(t.search("world"))
print(t.search("word"))
print(t.search("wordx"))


            
            
                
            
