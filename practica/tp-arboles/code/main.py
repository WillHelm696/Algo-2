from avltree import *

def print_tree_by_level(node):
    if node != None:
        print(node.value,"-",node.bf,",")
        print_tree_by_level(node.leftnode)
        print_tree_by_level(node.rightnode)

print("arboles binarios de busqueda")
B=AVLTree()
insert(B,"E",5)
insert(B,"C",3)
insert(B,"B",2)
insert(B,"A",1)
insert(B,"D",4)
insert(B,"G",7)
insert(B,"F",6)
print("Arbol B")
print(print_tree_by_level(B.root))
print("AVL calculateBAlance")
calculateBalance(B)
print(print_tree_by_level(B.root))
print("AVL delete")
deleteKey(B,6)
print(print_tree_by_level(B.root))
###############################
Tree=AVLTree()
insert(Tree,"A",0),insert(Tree,"C",2),insert(Tree,"B",1)
print(print_tree_by_level(Tree.root))
recalculate_fb(Tree)
reBalance(Tree)
print(print_tree_by_level(Tree.root))