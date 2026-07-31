class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord=True
        

    def search(self, word: str) -> bool:
        cur = self.root
        return self.find(word, 0, cur)
        
    
    def find(self, word, i, node):
        if i >= len(word):
            return node.endOfWord

        if word[i] == ".":
            if not node.children: # is empty?
                return False

            for c in node.children:
                if self.find(word, i + 1, node.children[c]):
                    return True
            return False
                

        if word[i] not in node.children:
            return False

        node = node.children[word[i]]
        return self.find(word, i + 1, node)
        
        
