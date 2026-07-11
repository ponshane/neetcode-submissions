class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            
            curr = curr.children[word[i]]

            if i == len(word) - 1:
                curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            
            if word[i] not in curr.children:
                return False
            
            curr = curr.children[word[i]]

            if i == len(word) - 1:
                if curr.end_of_word == False:
                    return False 
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            
            if prefix[i] not in curr.children:
                return False
            
            curr = curr.children[prefix[i]]
        return True
        