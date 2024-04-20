
class dictionarynode:
    value=None
    key:None
    nextNode=None

class dictionary:
    head=None

""" Descripción: Inserta un key en una posición determinada por la función de hash (1) en el diccionario (dictionary). Resolver colisiones por
    encadenamiento. En caso de keys duplicados se anexan a la lista.
    Entrada: el diccionario sobre el cual se quiere realizar la inserción
    y el valor del key a insertar
    Salida: Devuelve D
""""
def h(k,m):
    return (k % m)

def add_hash(current,node):
    if current.nextNode is None:
        current.nextNode=node
    else:
        add_hash(current.nextNode,node)

def insert(D,key, value):
    m=len(D.head) # El diccionario sera una lista array y el encadenamiento sera de tipo linkedLit
    if m > 0 :
        node=dictionary
        node.value=value
        node.key=key
        idx=h(k,m)
        if D.head[idx] is None 
            D.head[idx]=node
        else:
            add_hash(D.head[idx],node)
    return D
""" Descripción: Busca un key en el diccionario
    Entrada: El diccionario sobre el cual se quiere realizar la búsqueda
    (dictionary) y el valor del key a buscar.
    Salida: Devuelve el value de la key. Devuelve None si el key no se
    encuentra.
"""
def google(current,key):
    if current!=None:
        if current.key == key:
            return current[idx].value
        else:
            return (current.nextNode,key)
    return None

def search(D,key):    
    m=len(D.head)
    if m > 0 :
        idx=h(k,m)
        return google(D.head[idx],key)
    return None
""" Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary)
    Poscondición: Se debe marcar como nulo el key a eliminar.
    Entrada: El diccionario sobre el se quiere realizar la eliminación y
    el valor del key que se va a eliminar.
    Salida: Devuelve D 
"""
def delete_key(current,key):
    if current.nextNode != None:
        if current.nextNode.key==key:
            current.nextNode=current.nextNode.nextNode
        else:
            delete_key(current.nextNode,key)
    return None

def delete(D,key):
    m=len(D.head)
    if m > 0 :
        idx=h(k,m)
        if D.hed[idx].key=key:
            D.head[idx]= D.head[idx].nextNode
        return delete_key(D.head[idx],key)
    return None
