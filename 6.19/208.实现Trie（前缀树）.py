class TrieNode:
    def __init__(self):
        self.isWord=False
        self.children=dict()
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node=self.root
        for c in word:
            child=node.children.get(c)
            if not child:
                child=TrieNode()
                node.children[c]=child
            node=child
        node.isWord=True
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node=self.root
        for c in word:
            child=node.children.get(c)
            if not child:
                return False
            node=child
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node=self.root
        for c in prefix:
            child=node.children.get(c)
            if not child:
                return False
            node=child
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)