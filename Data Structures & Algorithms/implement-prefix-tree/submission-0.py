class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children: # not in children
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.isLast = True



    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isLast

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True if cur.children else False
        
        