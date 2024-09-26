class Node:
    def __init__(self):
        self.children = {}
        self.isLeafNode = False
        self.index = None


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, index, current=None): 
        if current is None: # first iteration  
            current = self.root
        if not word: # all the word is inserted =>word=none
            current.isLeafNode = True # end of the word
            current.index = index
        else:
            char = word[0] # b
            if char not in current.children:
                current.children[char] = Node()
            self.insert(word[1:], index, current.children[char])



    def search(self, search_val, level =0, current = None):#char #buy

        if level == 0: # first iteration
            current =self.root

        if level == len(search_val): # all the word is searched
            if current.isLeafNode: # if true  = end of a word
                return current.index
            else:
                return None # subword => none

        char = search_val[level] # level 0 => char 0 and so on...
        if current.children[char] is None: # the branch is done without finding the whole word
            return None
        return self.search(search_val, level + 1 ,current.children[char])


    def collect(self):
        words = []
        self.collect_helper(self.root, words)
        print(words) 

    def collect_helper(self,current, words, current_word=""):
        if current.isLeafNode:
            words.append((current_word,current.index)) # tuple of word and its index

        for char, child in current.children.items():
            self.collect_helper(child, words, current_word + char) #by

    def suggest(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.get_words_with_prefix(node, prefix)

    def get_words_with_prefix(self, node, current_prefix):
        suggestions = []
        if node.isLeafNode:
            suggestions.append(current_prefix)
        for char, child_node in node.children.items():
            suggestions.extend(self.get_words_with_prefix(child_node, current_prefix + char))
        return suggestions




"""

--time complexity:

^ insertion:
O(L) => L => length of the word

^ search:
O(L) => L => length of the word

^ collect:
O(total number of nodes in the Trie)



--space complexity of all the trie:

O(total number of nodes in the Trie).
+
additional space used during the collection process to store the collected words.
In the worst case, this could be O(total number of nodes in the Trie). (each word is a one char)
"""
