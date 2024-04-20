class Trie:
	root = None

class TrieNode: 
    parent = None
    children = None   
    key = None
    isEndOfWord = False
####################################################################################
def insert(T, string):
    if T.root is None:
        newNode = TrieNode()
        #print("Insertado",string[0])
        newNode.key = string[0]
        newNode.children = [None, None]
        T.root = newNode
        if len(string) == 1:
            T.root.isEndOfWord = True
    add(T.root, string)

def add(current,string):
    if current is not None:
        if current.key == string[0]:
            string=string[1:]
            if not string:
                return
            elif current.children[0] != None:
                #print("Hijo de",current.key)
                return add(current.children[0],string)
            else:
                newNode = TrieNode()
                newNode.parent=current
                #print("Insertado como Hijo",string[0])
                newNode.key = string[0]
                newNode.children = [None, None]
                current.children[0] = newNode
                if len(string) == 1:
                    newNode.isEndOfWord = True
            return add(current.children[0],string)
        if current.children[1] != None:
            #print(current.key,"Hermano de",current.children[1].key)
            return add(current.children[1],string)
        else:
            newNode = TrieNode()
            newNode.parent=current
            #print("Insertado como hermano",string[0])
            newNode.key = string[0]
            newNode.children = [None, None]
            current.children[1] = newNode
            if len(string) == 1:
                newNode.isEndOfWord = True
        #print(current.key,"Hermano de",current.children[1].key)
        return add(current.children[1],string)
####################################################################################
def find(current,string):
    if current is None and len(string) > 0:
        return False
    elif current is None and len(string) == 0:
        return True
    if current.key == string[0]:
        #print("Buscar hijo",current.key)
        return find(current.children[0],string[1:])
    else:
        #print("Buscar hermano",current.key)
        return find(current.children[1],string)

def search(T,string):
    if T.root != None:
        return find(T.root,string)
    return False
####################################################################################
"""
Ejercicio 3
delete(T,element)
	Descripción: Elimina un elemento se encuentre dentro del Trie
    Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
    Salida: Devuelve False o True  según se haya eliminado el elemento.
"""
def delete_word(current,element):
    if current is None and len(element) > 0:
        return False
    elif current is None and len(element) == 0:
        return True
    # Recorrer ambos hijos: [0] es el hijo directo y [1] es el hermano
    if current.key == element[0]:
        Flag = delete_word(current.children[0],element[1:])
        if Flag == True and current.children[1] is None:
            if current.isEndOfWord == False and len(element) > 1:
                if current.children[0].key == element[1]:
                    print (current.children[0].key,element[1])
                    current.children[0]=None
                print (current.key,element[0])
    else:
        Flag = delete_word(current.children[1],element)
        if Flag == True and current.children[0] is None:
            if current.isEndOfWord == False and len(element) > 1:
                if current.children[1].key == element[1]:
                    print (current.children[1].key,element[1])
                    current.children[0]=None
                print (current.key,element[0])
    # Si es el final de una palabra, agregar al resultado
    return Flag

def delete(T,element):
    if T.root !=None:
        return delete_word(T.root,element)
    return False
####################################################################################
"""
Ejercicio 4
Implementar un algoritmo que dado un árbol Trie T, un patrón p (prefijo) y un entero n, escriba 
todas las palabras del árbol que empiezan por p y sean de longitud n. 
"""
def collect_prefj(node,prfj,n, prefix, words):
    if node is None:
        return
    # Agregar la clave actual al prefijo
    new_prefix = prefix + node.key if node.key else prefix
    # Si es el final de una palabra, agregar al resultado
    if node.isEndOfWord:
        if new_prefix[0] == prfj[0] and len(new_prefix) == n: 
            words.append(new_prefix)
    # Recorrer ambos hijos: [0] es el hijo directo y [1] es el hermano
    collect_prefj(node.children[0],prfj,n, new_prefix, words)
    collect_prefj(node.children[1],prfj,n, prefix, words)  # note que se usa el prefijo sin añadir la clave actual

def prefj(T,prfj,n):
    words = []
    collect_prefj(T.root,prfj,n,"", words)
    return words
####################################################################################
"""
Ejercicio 5
Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo 
documento y False en caso contrario. Se considera que un  Trie pertenece al mismo documento cuando:
1-Ambos Trie sean iguales (esto se debe cumplir)
2-El Trie T1 contiene un subconjunto de las palabras del Trie T2 
3-Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.
"""
def is_subset(T2,L1):
    for i in L1:
        if not search(T2,i) :
            return False
    return True

def compare_tries(T1, T2):
    if T1.root is not None and T2.root is not None:
        #Compara dos Tries y determina si son iguales o si uno es subconjunto del otro.
        List1=get_all_words(T1) 
        if len(List1)>0 or T1.root is not None:            
            return is_subset(T2,List1)
    return False
####################################################################################
"""
Ejercicio 6
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. Dos cadenas son 
invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee de derecha a izquierda, ej: abcd 
y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren en un carácter.
"""
def generate_reverse(word):
    return word[::-1] #Funcional que invierte una lista

def search_inverted(T,words):
    for list in words:
        l1=generate_reverse(list)
        if search(T,l1):
            return True
    return False

def is_inverted_pair(T):
    if T.root is None:
        return False
    list = get_all_words(T)
    return search_inverted(T,list)
"""
Ejercicio 7
Un corrector ortográfico interactivo utiliza un Trie para representar las palabras de su diccionario. Queremos añadir una 
función de auto-completar (al estilo de la tecla TAB en Linux): cuando estamos a medio escribir una palabra, si sólo existe 
una forma correcta de continuarla entonces debemos indicarlo. 
Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y la cadena  
devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) devolvería “land”, 
ya que podemos tener “groenlandia” o “groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al 
documento que representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. 
Por ejemplo, autoCompletar(T, ma’) devolvería “” (cadena vacia) si T presenta las cadenas “madera” y “mama”. 
"""
####################################################################################
def collect_words(node, prefix, words):
    if node is None:
        return
    # Agregar la clave actual al prefijo
    new_prefix = prefix + node.key if node.key else prefix
    # Si es el final de una palabra, agregar al resultado
    if node.isEndOfWord:
        words.append(new_prefix)
    # Recorrer ambos hijos: [0] es el hijo directo y [1] es el hermano
    collect_words(node.children[0], new_prefix, words)
    collect_words(node.children[1], prefix, words)  # note que se usa el prefijo sin añadir la clave actual

def get_all_words(T):
    words = []
    collect_words(T.root, "", words)
    return words

