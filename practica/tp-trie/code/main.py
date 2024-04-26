from triee import *

T=Trie()
print("Ejercicio_1-------------------------")
insert(T,"cris")
insert(T,"cruz")
insert(T,"javi")
insert(T,"juan")
insert(T,"rafa")
all_words = get_all_words(T)
print("Trie 0:",all_words)
print("Ejercicio_2-------------------------")
print("buscar 'cris'",search(T,"cris"))
print("buscar 'cruz'",search(T,"cruz"))
print("buscar 'javi'",search(T,"javi"))
print("buscar 'juan'",search(T,"juan"))
print("buscar 'rafa'",search(T,"rafa"))
print("Ejercio_3-------------------------")
A=delete(T,"cris")
print("delete 'cris':",A)
all_words = get_all_words(T)
print(all_words)
####################################################################################
""" Ejercicio 4
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

print("Ejercio_4-------------------------")
B=prefj(T,"j",4)
print("prefijo de j:",B)
####################################################################################
""" Ejercicio 5
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

print("Ejercio_5-------------------------")
T1=Trie()
insert(T1,"rafa")
insert(T1,"javi")
insert(T1,"cruz")
all_words =get_all_words(T)
print("Trie 0:",all_words)
all_words =get_all_words(T1)
print("Trie 1:",all_words)
A=compare_tries(T1,T)
print(A)
####################################################################################
""" Ejercicio 6
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

print("Ejercio_6-------------------------")
insert(T1,"afar")
all_words = get_all_words(T1)
print("Trie 1:",all_words)
print(is_inverted_pair(T1))

""" Ejercicio 7
    Un corrector ortográfico interactivo utiliza un Trie para representar las palabras de su diccionario. Queremos añadir una 
    función de auto-completar (al estilo de la tecla TAB en Linux): cuando estamos a medio escribir una palabra, si sólo existe 
    una forma correcta de continuarla entonces debemos indicarlo. 
    Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y la cadena  
    devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) devolvería “land”, 
    ya que podemos tener “groenlandia” o “groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al 
    documento que representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. 
    Por ejemplo, autoCompletar(T, ma’) devolvería “” (cadena vacia) si T presenta las cadenas “madera” y “mama”. 
"""
def completar(current,element,words):
    if current is not None:
        if len(element) > 0:
            if current.key==element[0]:
                print("0",current.key)
                return completar(current.children[0],element[1:],words)
            else:
                print("1",current.key)
                return completar(current.children[1],element,words)
        else:
            print(current.key,current.isEndOfWord,current.children)

            if current.isEndOfWord != False and current.children == [None,None]: 
                new_words = words + current.key if current.key else words
                print(words)
                return words
            else:
                new_words = words + current.key if current.key else words
                if current.children[0] is not None or current.children[1] is not None:
                    print(new_words)
                    if current.children[0] is not None and current.children[1] is None:
                        return completar(current.children[0],element,new_words)
                    elif current.children[0] is None and current.children[1] is not None:
                        return completar(current.children[1],element,new_words)
                
            return "-"
    return words

def autoCompletar(T,cadena):
    if T.root!= None:
        return completar(T.root,cadena,"-")
    return "-"

print("Ejercio_7-------------------------")

A=autoCompletar(T,"jav")
print("jav:",A)