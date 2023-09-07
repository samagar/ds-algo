# Data Structure

'''  TRIE - Short for ReTRIEval '''
# Tree Structure with every node as a Dict keeping list of chars, & children chars
# Best datastructure for string serch

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstr = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def InsertStr(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofstr = True
        print("Successfully inserted")
    
    def SearchString(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node

        if current.endofstr == True:
            return True
        else:
            return False
        
    def __repr__(self):
        def recur(node, indent):
            return "".join(indent + key + ("." if child.endofstr else "") 
                                  + recur(child, indent +  " " ) 
                for key, child in node.children.items())

        return recur(self.root, "\n ")

def DeleteString(root, word, index):
    ch = word[index]
    current = root.children.get(ch)
    CanThisNodeBeDeleted = False

    if len(current.children) > 1:
        DeleteString(current, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(current.children) >= 1:
            current.endofstr = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if current.endofstr == True:
        DeleteString(current, word, index+1)
        return False

    CanThisNodeBeDeleted = DeleteString(current, word, index+1)
    
    if CanThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

newTrie = Trie()
newTrie.InsertStr("App")
newTrie.InsertStr("Appl")
newTrie.InsertStr("Amala")
newTrie.InsertStr("Amarapali")
newTrie.InsertStr("sandeep")
newTrie.InsertStr("sanidali")
newTrie.InsertStr("Ashtavinayak")
DeleteString(newTrie.root, "App", 0)
print(newTrie.SearchString("App"))
print(newTrie)