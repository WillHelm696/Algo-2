class Trie:
	root = None

class TrieNode: 
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def insert(T,string):
    if T.root != None:
        newNode=TrieNode()
        newNode.key= string[0]
        newNode.children={}
        T.root=newNode
    add (T.root,string[1:])

def add(current,string):
    if current.children == None:
        newNode=TrieNode()
        newNode.key=string[0]
        current.children={}
        current.children=newNode
        if len(string)==1 :
            isEndOfWord = True
            return
        add (current.children[0],string[1:])
    else:
        if (current.key == string[0]):
            add(current.children[0],string[1:])
        else:            
            current.children.append({})
            add(current.children[1],string[1:])

def search(T,element):
    if T.root != None:
        find(T.root,element)
    return False

def find(current,string):
    if current.key == string[0]:
        if len(string)== 1:
            return current.isEndOfWord
        find(current.children[0],string[1:])
    return False