from avltree import *
from collections import deque
def print_tree_by_level(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.value, "-bf:", node.bf, "-h:", node.height, "-cnt:", node.count, ",")
        if node.leftnode:
            queue.append(node.leftnode)
        if node.rightnode:
            queue.append(node.rightnode)

print("AVL arboles binarios de busqueda")
print("Doble Rotate-----------------------------------------------------------")
Tree=AVLTree()
insert(Tree,"A",0)
print(print_tree_by_level(Tree.root))
insert(Tree,"C",2)
print(print_tree_by_level(Tree.root))
insert(Tree,"B",1)
print(print_tree_by_level(Tree.root))
print("AVL B-----------------------------------------------------------")
B=AVLTree()
print("Arbol B")
insert(B,"E",5)
print(print_tree_by_level(B.root))
insert(B,"C",3)
print(print_tree_by_level(B.root))
insert(B,"B",2)
print(print_tree_by_level(B.root))
insert(B,"A",1)
print(print_tree_by_level(B.root))
insert(B,"D",4)
print(print_tree_by_level(B.root))
insert(B,"G",7)
print(print_tree_by_level(B.root))
insert(B,"F",6)
print(print_tree_by_level(B.root))
print("AVL delete A-----------------------------------------------------------")
deleteKey(B,1)
print(print_tree_by_level(B.root))