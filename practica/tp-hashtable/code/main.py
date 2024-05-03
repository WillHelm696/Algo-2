from dictionary import *
""" Ejercicio 2 """
D=dictionary()
D.head=[None]*9
D = insert(D,5,"valor1")
D = insert(D,28,"valor2")
D = insert(D,19,"valor3")
D = insert(D,15,"valor4")
D = insert(D,20,"valor5")
D = insert(D,33,"valor6")
D = insert(D,12,"valor7")
D = insert(D,17,"valor8")
D = insert(D,10,"valor9")
print_dictionary(D)
print("-------------------------------------------------------------------------------------")
print(search(D,20))
print(search(D,10))
print("-------------------------------------------------------------------------------------")
delete(D,19)
print("elimina 19")
delete(D,15)
print("elimina 15",)
print_dictionary(D)
""" Ejercicio 4
    Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente
    proposición: dado dos strings s1...sk y p1...pk, se quiere encontrar si los caracteres de p1...pk
    corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.
"""
def insert_hash(current,node):
    if current.nextNode is None:
        current.nextNode=node
    else:
        add_hash(current.nextNode,node)

def table_hash(D,key, value):
    m=len(D.head) # El diccionario sera una lista array y el encadenamiento sera de tipo linkedLit
    if m > 0 :
        node=dictionarynode()
        node.value=value
        node.key=key
        idx=h(key,m)
        if D.head[idx] is None:
            D.head[idx]=node
        elif D.head[idx] is not None:
            add_hash(D.head[idx],node)
    return D

def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1=list1.lower()
    list2=list2.lower()
    T=dictionary()
    T.head=[None]*len(list1)
    for char in list1:
        table_hash(T,ord(char),char)
    for char in list2:
        delete(T,ord(char))
    for node in T.head:
        if node is not None:
            return False
    return True
# Complejidad O(n): toma O(n) en recorer la lista para isertar en la tabla hash la lista1 y O(n) en recorer la lista2 y eliminarla de la tabla hash   
print("-------------------------------------------------------------------------------------")
A="1231234"
B="3213214"
print(A," y ",B," son permutaciones")
print(permutation(A,B))
######################################################################################
""" Ejercicio 5
    Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus
    elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución
    propuesta.
"""
def list_unico(lst):
    m=len(lst)
    S=dictionary()
    S.head=[None]*m
    for key in lst:
        if search(S,key) == key:  
            return False
        insert(S,key,key)
    return True
print("-------------------------------------------------------------------------------------")
L=[1,5,12,1,2]
print(L," es unico",list_unico(L))
######################################################################################
""" Ejercicio 6
    Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter
    (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que
    representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e
    implementar una función de hash apropiada para los códigos postales argentinos.
"""
def cod_postal(list):
        
        return
######################################################################################
""" Ejercicio 7
    Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el
    recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en
    ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su
    método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras
    mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.
"""
def list_cont(current):
    cont=1
    while current.nextNode != None:
        cont+=1
        current=current.nextNode
    return cont

def list_comprimida(list):
    if len(list)>0:
        C=dictionary()
        C.head=[None]*24
        for char in list:
            table_hash(C,ord(char),char)
        new_list=""
        for current in C.head:
            if current is not None:
                n=list_cont(current)
                new_list += current.value
                if n > 1:
                    new_list += str(n)
        return new_list
    return list
print("-------------------------------------------------------------------------------------")
Cadena="aabcccccaaa"
print(Cadena)
print("Comprimido:",list_comprimida(Cadena))
######################################################################################
""" Ejercicio 8
    Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar 
    esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución 
    por fuerza bruta). Justificar el coste en tiempo de la solución propuesta. 
"""
######################################################################################
"""
Ejercicio 9 
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}.
Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). 
¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto? 
"""
######################################################################################
