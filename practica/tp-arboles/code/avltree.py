import math

class AVLTree:
     root = None

class AVLNode:
	parent = None
	leftnode = None
	rightnode = None
	key = None
	value = None
	count = None
	height = None # Haltura del nodo
	bf = None # Balance Factor del Nodo 
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
'------------------------------------------------------------'
# Función para calcular la altura de un nodo en el árbol. Tiene complegidad O(n)
# Se implemento para las pruebas del los ejercicio y luego se quito 
def haltura(avlnode):
    if avlnode is not None:
        left_height = haltura(avlnode.leftnode)
        right_height = haltura(avlnode.rightnode)
        # La altura del árbol es la altura máxima de sus subárboles más 1
        return max(left_height, right_height) + 1
    return 0
#////////////////////////////////////////////////////////////////////////
def rotateLeft(Tree,avlnode): 
	# Función para rotar el árbol hacia la izquierda.
	new_root = avlnode.rightnode
	avlnode.rightnode = new_root.leftnode
	if new_root.leftnode:
		new_root.leftnode.parent = avlnode
	new_root.parent = avlnode.parent
	if not avlnode.parent:
		Tree.root = new_root
	elif avlnode == avlnode.parent.leftnode:
		avlnode.parent.leftnode = new_root
	else:
		avlnode.parent.rightnode = new_root
	new_root.leftnode = avlnode
	avlnode.parent = new_root
	return new_root
        
def rotateRight(Tree,avlnode):
	# Función para rotar el árbol hacia la Derecha.
	new_root = avlnode.leftnode
	avlnode.leftnode = new_root.rightnode
	if new_root.rightnode:
		new_root.rightnode.parent = avlnode
	new_root.parent = avlnode.parent
	if not avlnode.parent:
		Tree.root = new_root
	elif avlnode == avlnode.parent.rightnode:
		avlnode.parent.rightnode = new_root
	else:
		avlnode.parent.leftnode = new_root
	new_root.rightnode = avlnode
	avlnode.parent = new_root
	return new_root
#////////////////////////////////////////////////////////////////////////
def calculateBalance(AVLTree): # Implementación para calcular el balance de los nodos del árbol...
    if AVLTree.root!=None:
        calculate_bf(AVLTree.root) 
    return AVLTree

def calculate_bf(avlnode):
	if avlnode !=None: # Trabaja desde el ultimo nodo hacia lariz para cada nodo hoja
		avlnode.bf = bf(avlnode)
		calculate_bf(avlnode.leftnode)
		calculate_bf(avlnode.rightnode)

def bf(avlnode):
    left_height = avlnode.leftnode.height if avlnode.leftnode else 0 # Utiliza la haltura del nodo Izquierdo
    right_height = avlnode.rightnode.height if avlnode.rightnode else 0 # Utiliza la haltura del nodo Derecho
    return left_height - right_height # Retorna el calculo del bf 
#////////////////////////////////////////////////////////////////////////
def reBalance(AVLTree):
    if AVLTree.root!=None:
        recalculate_fb(AVLTree,AVLTree.root)
    return AVLTree
# La funcion recalcula el Balans Factor de cada nodo empezando desde el nodo hoja hasta la raiz para cada hohja
def recalculate_fb(AVLTree,avlnode):
	if avlnode !=None:
		avlnode.leftnode=recalculate_fb(AVLTree,avlnode.leftnode)
		avlnode.rightnode=recalculate_fb(AVLTree,avlnode.rightnode)
		avlnode.bf = bf(avlnode) # Funcion que calcula el Balans Factor
		if avlnode.bf < -1 or 1 < avlnode.bf : # Una vez calculado verifica su bf
			if avlnode.bf < 0 : # Si es -2  o menos hace una rotacion a izquierda
				if avlnode.rightnode.bf > 0:
					avlnode.rightnode=rotateRight(AVLTree,avlnode.rightnode)
					update_height(avlnode.rightnode.rightnode)
					update_count(avlnode.rightnode.rightnode)
				new_root = rotateLeft(AVLTree,avlnode)
			elif avlnode.bf > 0 :
				if avlnode.leftnode.bf < 0:
						avlnode.leftnode=rotateLeft(AVLTree,avlnode.leftnode)
						update_count(avlnode.leftnode.leftnode)
						update_height(avlnode.leftnode.leftnode)
				new_root = rotateRight(AVLTree,avlnode)
			update_height(avlnode)
			update_count(avlnode)
			recalculate_fb(AVLTree,new_root)
			return new_root
#////////////////////////////////////////////////////////////////////////
def insert(B,element,key):
	avlnode = AVLNode()
	avlnode.value = element
	avlnode.key = key
	avlnode.height = 0
	avlnode.count = 0
	avlnode.bf = 0
	if B.root==None:
			B.root=avlnode
			return key
	node = Add_Node(B.root,avlnode)
	update_height(avlnode)
	update_count(avlnode)
	update_bf(B,avlnode)
	return node.key

def Add_Node(Current,avlnode):
	if Current.key > avlnode.key:
		Current.count +=1
		if Current.leftnode==None:
			Current.leftnode=avlnode
			avlnode.parent=Current
		else:
			return Add_Node(Current.leftnode,avlnode)
	elif Current.key < avlnode.key :
		Current.count +=1
		if Current.rightnode==None:
			Current.rightnode=avlnode
			avlnode.parent=Current
		else:
			return Add_Node(Current.rightnode,avlnode)
	return avlnode
'------------------------------------------------------------'
# Utilizado en la funciones de insercion y eliminacion y ReBalanceo
def update_bf(B, avlnode): # Esta funcio actualiza los nodos insertados y eliminados  hasta la raiz
	if avlnode is not None:
		avlnode.bf = bf(avlnode)
		if avlnode.bf < -1 or 1 < avlnode.bf:
			if avlnode.bf < 0:
				if avlnode.rightnode.bf > 0:
					avlnode.rightnode = rotateRight(B, avlnode.rightnode)
					update_height(avlnode.rightnode.rightnode)
					update_count(avlnode.rightnode.rightnode)
				avlnode = rotateLeft(B, avlnode)
			elif avlnode.bf > 0:
				if avlnode.leftnode.bf < 0:
					avlnode.leftnode = rotateLeft(B, avlnode.leftnode)
					update_height(avlnode.leftnode.leftnode)
					update_count(avlnode.leftnode.leftnode)
				avlnode = rotateRight(B, avlnode)
			update_height(avlnode)
			update_count(avlnode)
		update_bf(B, avlnode.parent)

def update_height(node): # Esta funcion actualiza la haltura de forma recursiva hasta la rais
    if node is not None: 
        left_height = node.leftnode.height if node.leftnode else 0
        right_height = node.rightnode.height if node.rightnode else 0
        node.height = max(left_height, right_height) + 1
        update_height(node.parent)

def update_count(node): # La funcion actualiza la cantidad de nodos que tiene como sub arbol hasta la raiz
    if node is not None:
        left_count = node.leftnode.count if node.leftnode else 0
        right_count = node.rightnode.count if node.rightnode else 0
        node.count = left_count + right_count
        update_height(node.parent)
#////////////////////////////////////////////////////////////////////////
def delete(B,element):
	key=search(B,element)
	if key!=None:
		return deleteKey(B,key)
	return None
# 
def deleteKey(B, key):
    if access(B, key) is not None:
        B.root = delete_node(B,B.root, key)
        return key
    return None

def delete_node(B,node, key):
	if node is None:
		return node
	if key < node.key:
		node.leftnode = delete_node(B,node.leftnode, key)
	elif key > node.key:
		node.rightnode = delete_node(B,node.rightnode, key)
	else:
		if node.leftnode is None:
			temp = node.rightnode
			node = None
			return temp
		elif node.rightnode is None:
			temp = node.leftnode
			node = None
			return temp
		temp = min_node(node.rightnode)
		node.key = temp.key
		node.rightnode = delete_node(B,node.rightnode,temp.key)
	update_height(node)
	update_count(node)
	update_bf(B,node)	
	return node

def min_node(node):
    current = node
    while current.leftnode is not None:
        current = current.leftnode
    return current

