
class dictionary:
    head=None

class dictionarynode:
    value=None
    key=None
    nextNode=None
    count=1
######################################################################################
""" Descripción: Inserta un key en una posición determinada por la función de hash (1) en el diccionario (dictionary). Resolver colisiones por
    encadenamiento. En caso de keys duplicados se anexan a la lista.
    Entrada: el diccionario sobre el cual se quiere realizar la inserción
    y el valor del key a insertar
    Salida: Devuelve D
"""
def h(k,m):
    return (k % m)

def add_hash(current,node):
    if current.key == node.key and current.value == node.value:
        current.count += 1
        
    elif current.nextNode is None:
        current.nextNode=node
    else:
        if current.key != node.key and current.value != node.value:
            add_hash(current.nextNode,node)

def insert(D,key, value):
    m=len(D.head) # El diccionario sera una lista array y el encadenamiento sera de tipo linkedLit
    if m > 0 :
        node=dictionarynode()
        node.value=value
        node.key=key
        idx=h(key,m)
        if D.head[idx] is None:
            D.head[idx]=node
        elif D.head[idx] is not None:
            if D.head[idx].key != key and D.head[idx].value != value:
                add_hash(D.head[idx],node)
            else:
                D.head[idx].count += 1
    return D
######################################################################################
""" Descripción: Busca un key en el diccionario
    Entrada: El diccionario sobre el cual se quiere realizar la búsqueda
    (dictionary) y el valor del key a buscar.
    Salida: Devuelve el value de la key. Devuelve None si el key no se
    encuentra.
"""
def google(current,key):
    if current!=None:
        if current.key == key:
            return current.value
        else:
            return google(current.nextNode,key)
    return None

def search(D,key):
    m=len(D.head)
    if m > 0 :
        idx=h(key,m)
        return google(D.head[idx],key)
    return None
######################################################################################
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
            return delete_key(current.nextNode,key)

def delete(D,key):
    m=len(D.head)
    if m > 0 :
        idx = h(key,m)
        if D.head[idx] is not None:
            if D.head[idx].key == key:
                D.head[idx]= D.head[idx].nextNode
                return D
            else:
                delete_key(D.head[idx],key)
    return D
######################################################################################
def print_dictionary(D):
    if D is None or D.head is None:
        print("El diccionario está vacío.")
        return    
    for idx, bucket in enumerate(D.head):
        if bucket is not None:
            print(f"Posición {idx}:",end='')
            current = bucket
            while current is not None:
                print(f"<Key: {current.key}, Value: {current.value}> ",end='')
                current = current.nextNode
            print("")
        else:
            print(f"Posición {idx}: Vacía")
