from avltree import *

#Descripción: Implementa la operación rotación a la izquierda
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la izquierda
#Salida: retorna la nueva raíz
def rotateLeft(Tree,avlnode):
    newRoot=avlnode.rightnode
    newRoot.parent=avlnode.parent
    if avlnode.rightnode.leftnode !=None:
        avlnode.leftnode=newRoot.rightnode
        newRoot.rightnode.parent=avlnode
        avlnode.parent=newRoot
        newRoot.rightnode=avlnode
    
    else
        avlnode.leftnode=None
        newRoot.rightnode=avlnode
        avlnode.parent=newRoot
    return newRoot
        
#Descripción: Implementa la operación rotación a la derecha
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la derecha
#Salida: retorna la nueva raíz"""
def rotateRight(Tree,avlnode):
    newRoot=avlnode.leftnode
    newRoot.parent=avlnode.parent
    if avlnode.leftnode.rightnode !=None:
        avlnode.rightnode=newRoot.leftnode
        newRoot.leftnode.parent=avlnode
        avlnode.parent=newRoot
        newRoot.leftnode=avlnode
    
    else
        avlnode.rightnode=None
        newRoot.leftnode=avlnode
        avlnode.parent=newRoot
    return newRoot