from Ejercicio1 import *

class AVLTree:
     root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
'------------------------------------------------------------'
def insert(B,element,key):
	Node=AVLNode()
	Node.key=key
	Node.value=element
	if B.root==None:
			B.root=Node
			return key
	return Add_Node(B.root,Node)

def Add_Node(Current,Node):
	if Current.leftnode==None or Current.rightnode==None:
		if Node.key<Current.key and Current.leftnode==None:
			Current.leftnode=Node
		elif Current.key<Node.key and Current.rightnode==None:
			Current.rightnode=Node			
	elif Current.leftnode!=None or Current.rightnode!=None:		
		if Current.leftnode!=None:
			if Node.key<Current.key:
				return Add_Node(Current.leftnode,Node)
		if Current.rightnode!=None:
			if Current.key<Node.key:
				return Add_Node(Current.rightnode,Node)
	Node.parent=Current
	return Node.key
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
def delete(B,element):
	key=search(B,element)
	if key!=None:
		return deleteKey(B,key)
	return None 	
def deleteKey(B,key):
	if access(B,key)!=None:
		Nodo=Node_Raiz(B,key)
		return Nodo.key
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
'------------------------------------------------------------'
def balance_factor(avlnode):
	while avlnode != None:		
		if avlnode.leftnode == avlnode.rightnode :
			avlnode.bf = 0
		elif avlnode.leftnode.bf != None and avlnode.rightnode.bf == None: 
			avlnode.bf = avlnode.leftnode.bf+1 - 0 
		elif avlnode.leftnode.bf == None and avlnode.rightnode.bf != None: 
			avlnode.bf = 0 -( avlnode.leftnode.bf+1) 
		elif avlnode.bf>1 :
			rotateLeft(avlnode)
		else avlnode.bf<1
		

		avlnode = avlnode.parent