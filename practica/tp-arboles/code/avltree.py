import math

class AVLTree:
     root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
	height = None
	count = None
    bf = None
'------------------------------------------------------------'
def search(B,element):
	if B.root!=None:
		return Búsqueda(B.root,element)
	return None
def Búsqueda(Current,element):
	if Current!=None:
		if Current.value==element:
			return Current.key
		key=Búsqueda(Current.leftnode,element)
		if key==None:
			key=Búsqueda(Current.rightnode,element)
		return key
'------------------------------------------------------------'
def access(B,key):
	if B.root!=None:
		return Acceso(B.root,key)
	return None
def Acceso(Current,key):
	if Current!=None:
		if Current.key==key:
			return Current.value
		elif key<Current.key:
			return Acceso(Current.leftnode,key)
		elif Current.key<key:
			return Acceso(Current.rightnode,key)
	return None
'------------------------------------------------------------'
def update(B,element,key):
	if B.root!=None:
		return Actualizar(B.root,element,key)
	return None
def Actualizar(Current,element,key):
	if Current!=None:
		if Current.key==key:
			Current.value=element
			return Current.key
		elif key<Current.key:
			return Actualizar(Current.leftnode,element,key)
		elif Current.key<key:
			return Actualizar(Current.rightnode,element,key)
	return None
#////////////////////////////////////////////////////////////////////////

def rotateLeft(node):
    new_root = node.rightnode
    node.rightnode = new_root.leftnode
    if new_root.leftnode:
        new_root.leftnode.parent = node
    new_root.parent = node.parent
    if not node.parent:
        root = new_root
    elif node == node.parent.leftnode:
        node.parent.leftnode = new_root
    else:
        node.parent.rightnode = new_root
    new_root.leftnode = node
    node.parent = new_root
    node.height = max(node.leftnode.height,node.rightnode.height) + 1
    new_root.height = max(new_root.leftnode.height,new_root.rightnode.height) + 1
    return new_root

def rotateRight(node):
    new_root = node.leftnode
    node.leftnode = new_root.rightnode
    if new_root.rightnode:
        new_root.rightnode.parent = node
    new_root.parent = node.parent
    if not node.parent:
        root = new_root
    elif node == node.parent.rightnode:
        node.parent.rightnode = new_root
    else:
        node.parent.leftnode = new_root
    new_root.rightnode = node
    node.parent = new_root
    node.height = max(node.leftnode.height,node.rightnode.height) + 1
    new_root.height = max(new_root.leftnode.height,new_root.rightnode.height) + 1
    return new_root

""""
def rotateLeft(Tree,avlnode):
	newRoot=avlnode.rightnode
	
	if avlnode.leftnode is None:
		if newRoot.leftnode != None:
			avlnode.rightnode = newRoot.leftnode
			#avlnode.rightnode.parent=avlnode
			newRoot.leftnode.rightnode = newRoot
			#newRoot.leftnode.righntnode.parent = newRoot.leftnode

			newRoot=avlnode.rightnode
		newRoot.leftnode=avlnode
		avlnode.rightnode=None
	else:
		avlnode.rightnode=newRoot.leftnode
		avlnode.rightnode.parent=avlnode

	if avlnode.parent == None:
		Tree.root=newRoot
	elif avlnode.parent.leftnode == avlnode:
		avlnode.parent.leftnode=newRoot
	else: 
		avlnode.parent.rightnode=newRoot

	newRoot.parent=avlnode.parent
	newRoot.leftnode = avlnode
	newRoot.leftnode.parent=newRoot##
	return newRoot

def rotateRight(Tree,avlnode):
	newRoot=avlnode.leftnode
	
	if avlnode.rightnode is None:
		if avlnode.leftnode.rightnode is not None:
			avlnode.leftnode = newRoot.rightnode
			newRoot.parent=newRoot.rightnode
			newRoot.rightnode.parent=avlnode
			avlnode.leftnode.leftnode=newRoot
			newRoot=avlnode.leftnode
		newRoot.rightnode=avlnode
		avlnode.leftnode=None
	else:
		avlnode.leftnode=newRoot.rightnode
		avlnode.leftnode.parent=avlnode

	if avlnode.parent == None:
		Tree.root=newRoot
	elif avlnode.parent.leftnode == avlnode:
		avlnode.parent.leftnode=newRoot
	else: 
		avlnode.parent.rightnode=newRoot

	newRoot.parent=avlnode.parent
	newRoot.rightnode = avlnode
	newRoot.rightnode.parent=newRoot##
	return newRoot
"""
#////////////////////////////////////////////////////////////////////////
def calculateBalance(AVLTree): 
    if AVLTree.root!=None:
        calculate_bf(AVLTree.root)
    return AVLTree

def calculate_bf(avlnode):
    if avlnode !=None:
        if avlnode.leftnode == avlnode.rightnode :
            avlnode.bf = 0
        avlnode.bf = haltura(avlnode.leftnode) - haltura(avlnode.rightnode)
        calculate_bf(avlnode.leftnode)
        calculate_bf(avlnode.rightnode)

def haltura(root):
    if root is not None:
        left_height = haltura(root.leftnode)
        right_height = haltura(root.rightnode)
        # La altura del árbol es la altura máxima de sus subárboles más 1
        return max(left_height, right_height) + 1
    return 0
#////////////////////////////////////////////////////////////////////////
def reBalance(AVLTree):
    if AVLTree.root!=None:
        recalculate_fb(AVLTree.root)
    return AVLTree

def recalculate_fb(avlnode):
	if avlnode !=None:
		recalculate_fb(avlnode.leftnode)
		recalculate_fb(avlnode.rightnode)
		if avlnode.leftnode == avlnode.rightnode :
			avlnode.bf = 0
		else:
			avlnode.bf = haltura(avlnode.leftnode) - haltura(avlnode.rightnode)

		if avlnode.bf > 1 :
			newRoot = rotateRight(avlnode)
		elif avlnode.bf < -1 :
			newRoot = rotateLeft(avlnode)
		recalculate_fb(newRoot)
	return newRoot
#////////////////////////////////////////////////////////////////////////
def insert(B,element,key):
	avlnode=AVLNode()
	avlnode.key=key
	avlnode.value=element
	avlnode.bf=0
	if B.root==None:
			B.root=avlnode
			return key
	return Add_Node(B.root,avlnode)

def Add_Node(Current,avlnode):
	if Current.leftnode==None or Current.rightnode==None:
		if avlnode.key<Current.key and Current.leftnode==None:
			Current.leftnode=avlnode
			update_bf(Current.leftnode)
		elif Current.key<avlnode.key and Current.rightnode==None:
			Current.rightnode=avlnode	
			update_bf(Current.rightnode)
	elif Current.leftnode!=None or Current.rightnode!=None:		
		if Current.leftnode!=None:
			if avlnode.key<Current.key:
				return Add_Node(Current.leftnode,avlnode)
		if Current.rightnode!=None:
			if Current.key<avlnode.key:
				return Add_Node(Current.rightnode,avlnode)
	avlnode.height = 1 + max(avlnode.leftnode.height,avlnode.righntnode.height)
	avlnode.parent=Current
	return avlnode.key

def update_bf(avlnode):
	if avlnode !=None:
		if avlnode.leftnode == avlnode.rightnode:
			avlnode.bf = 0
		else:
			avlnode.bf = haltura(avlnode.leftnode) - haltura(avlnode.rightnode)
		if avlnode.bf > 1 :
			newRoot = rotateRight(avlnode)
			recalculate_fb(newRoot)
		elif avlnode.bf < -1:
			newRoot = rotateLeft(avlnode)
			recalculate_fb(newRoot)
		return update_bf(avlnode.parent)
#////////////////////////////////////////////////////////////////////////
def delete(B,element):
	key=search(B,element)
	if key!=None:
		return deleteKey(B,key)
	return None

def deleteKey(B,key):
	if access(B,key)!=None:
		avlnode=Node_Raiz(B,key)
		balance_factor(avlnode.parent)
		return avlnode.key
	return None
'------------------------------------------------------------'
def Node_Raiz(B,key):
	if B.root.key==key:
		Node=B.root
		if Node.leftnode!=None or Node.rightnode!=None:
			B.root=Node_Interno(B.root,key)
		else:
			B.root=Node.leftnode 
		return Node
	return Node_Interno(B.root,key) 

def Node_Hoja(Node,key):
	Rama=Node.parent 
	if Rama.leftnode!=None:
		if Rama.leftnode.key==key:
			Rama.leftnode=Node.leftnode
	if Rama.rightnode!=None:
		if Rama.rightnode.key==key:
			Rama.rightnode=Node.rightnode
	return Node
	
def Node_Interno(Current,key):
	if Current!=None:
		if Current.key==key:
			Rama=Current
			Node=Current
			if Rama.leftnode==None and Rama.rightnode==None:
				return Node_Hoja(Current,key)
			elif Rama.leftnode!=None:
				Current=Current.leftnode
				while Current.rightnode!=None:
					Current=Current.rightnode					
			elif Rama.rightnode!=None:
				Current=Current.rightnode
				while Current.leftnode!=None:
					Current=Current.leftnode
			elif Current.rightnode!=None or Current.leftnode!=None:
				return Node_Interno(Current,Current.key)
			Hoja=Node_Hoja(Current,Current.key)
			Hoja.rightnode=Rama.rightnode
			Hoja.leftnode=Rama.leftnode
			Hoja.parent=Rama.parent
			if Rama.parent==None:
				return Hoja
			#--------------------	
			else:
				Rama=Hoja
			#--------------------					
		elif key<Current.key:
			return Node_Interno(Current.leftnode,key)
		elif Current.key<key:
			return Node_Interno(Current.rightnode,key)
	return Node
