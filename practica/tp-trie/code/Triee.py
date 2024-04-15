class Trie:
	root = None

class TrieNode: 
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def insert(T, string):
    if T.root is None:
        newNode = TrieNode()
        newNode.key = string[0]
        newNode.children = [None, None]
        if len(string) == 1:
            newNode[0].isEndOfWord = True
        T.root = newNode
        string = string[1:] 
    add(T.root.children, string)

def add(current, string):
    if len(string) == 0:
        return
    i = 0 if not current[0] else 1  # Intenta colocar en la primera posición disponible
    if current[i] is None:
        newNode = TrieNode()
        newNode.parent=current
        newNode.key = string[0]
        newNode.children = [None, None]
        current[i] = newNode
    else:
        # Si el nodo ya existe con la misma clave, sigue adelante
        if current[i].key != string[0]:
            return  # Conflictos en claves deberían manejarse mejor
    if len(string) == 1:
        current[i].isEndOfWord = True
    else:
        add(current[i].children, string[1:])

def search(T,string):
    if T.root != None:
        find(T.root,string)
    return False

def find(current,string):
    if current!=None:
        if current.isEndOfWord:
            return current.isEndOfWord

        if current.key == string[0]:
            find(current.children[0],string[1:])
        else:
            find(current.children[1],string[1:])
    return False

def delete(T,element):    
    return False

"""
delete(T,element)
	Descripción: Elimina un elemento se encuentre dentro del Trie
    Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
    Salida: Devuelve False o True  según se haya eliminado el elemento.

Ejercicio 4
Implementar un algoritmo que dado un árbol Trie T, un patrón p (prefijo) y un entero n, escriba 
todas las palabras del árbol que empiezan por p y sean de longitud n. 

Ejercicio 5
Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo 
documento y False en caso contrario. Se considera que un  Trie pertenece al mismo documento cuando:
1-Ambos Trie sean iguales (esto se debe cumplir)
2-El Trie T1 contiene un subconjunto de las palabras del Trie T2 
3-Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.

Ejercicio 6
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. Dos cadenas son 
invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee de derecha a izquierda, ej: abcd 
y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren en un carácter.

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

def print_words(T):
    print_words_from_node(T.root,"")

def print_words_from_node(node, current_word):
    if node is None:
        return
    
    current_word += node.key  # Agrega la clave del nodo actual a la palabra en construcción

    if node.isEndOfWord:
        print(current_word)  # Si es el final de una palabra, imprímela

    # Recursivamente recorre los posibles hijos (en este caso, dos debido a la limitación)
    for child in node.children:
        print_words_from_node(child, current_word)