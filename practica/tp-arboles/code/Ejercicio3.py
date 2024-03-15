from avltree import *


def reBalance(AVLTree):
    if AVLTree.root!=None:
        balance_factor(AVLTree.root)
    return AVLTree

def balance_factor(avlnode):
    if avlnode !=None:
        balance_factor(avlnode.leftnode)
        balance_factor(avlnode.rightnode)

        if avlnode.leftnode == avlnode.rightnode :
            avlnode.bf = 0
        elif avlnode.leftnode.bf != None and avlnode.rightnode.bf == None: 
            avlnode.bf = avlnode.leftnode.bf+1
        elif avlnode.leftnode.bf == None and avlnode.rightnode.bf != None: 
            avlnode.bf = avlnode.leftnode.bf+1 
        elif avlnode.leftnode.bf != None and avlnode.rightnode.bf != None: 
            avlnode.fb = haltura(avlnode.leftnode,0) - haltura(rightnode,0)
        elif avlnode.bf>1 :
            rotateLeft(avlnode)
        else avlnode.bf<1
            rotateRight(avlnode)

        elif avlnode.bf > 1:
            newRoot = rotateRight(avlnode)
            balance_factor(newRoot)
        elif avlnode.bf < -1:
            newRoot = rotateLeft(avlnode)
            balance_factor(newRoot)
    return avlnode

def haltura(avlnode,num):
    if avlnode!=None:
        haltura(avlnode.leftnode,num+1)
        if avlnode.rightnode!=None:
            return haltura(avltree.rightnode,num+1)
        return num + 1
    return num