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
def update_count(current, key, value):
    if current is None:
        return
    if current.key == key and current.value == value:
        current.count -= 1
    else:
        update_count(current.nextNode, key, value)
    return current.count

def delete_count(T,key,char):
    m=len(T.head)
    idx=h(key,m)
    if T.head[idx] is None:
        return None
    else:
        if update_count(T.head[idx],key,char) == 0:
            delete(T,key)

def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1=list1.lower()
    list2=list2.lower()
    T=dictionary()
    T.head=[None]*len(list1)
    for char in list1:
        insert(T,ord(char),char)
    for char in list2:
        delete_count(T,ord(char),char)
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
def hash_codigo_postal(codigo_postal):
    trio= codigo_postal[:3].upper()
    key=0
    for char in trio:
        key += ord(char)
    key *=1000
    return key 
######################################################################################
""" Ejercicio 7
    Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el
    recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en
    ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su
    método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras
    mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.
"""
def compres_string(list):
    if len(list)>1:
        comprimido=[]
        cont=1
        for n in range(1,len(list)):
            if list[n] == list[n-1]:
                cont +=1
            else:
                comprimido.append(list[n-1]+str(cont))
                cont=1
    comprimido.append(list[n-1]+str(cont))
    comprimido=''.join(comprimido)
    if len(list)<=len(comprimido):
        return list
    return comprimido
#Coste del Tiempo es O(n) 
print("-------------------------------------------------------------------------------------")
cadena="aabcccccaaa"
print(cadena)
print("Comprimido:",compres_string(cadena))
######################################################################################
""" Ejercicio 8
    Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar 
    esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución 
    por fuerza bruta). Justificar el coste en tiempo de la solución propuesta. 
"""
def Karp_key(s,primo):
    key=0
    for n in range (0,len(s)):
        key += ord(s[n])*(primo**n)
    return key

def Rabin_Karp(p,a):
    k=len(p)
    l=len(a)
    primo=3
    if k>l:
        cadena=p[:l]
        key = Karp_key(cadena,primo)
        key_a = Karp_key(a,primo)
        for n in range(l,k):
            key = (key-ord(cadena[0]))/primo + ord(p[n])*(primo**(l-1))
            cadena = cadena[1:]+p[n]
            if key_a == key and a == cadena:
                return n-l+1
    return -1
# COmplejudad temporal O(K+L)
print("-------------------------------------------------------------------------------------")
p='abracadabra'
a='cada'
print(a," es ocurencia de ",p,"en:")
print(Rabin_Karp(p,a))
######################################################################################
"""
Ejercicio 9 
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}.
Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). 
¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto? 
"""
def is_subset(S,T):
    Q=dictionary()
    Q.head=[None]*len(S)
    for element in S:
        insert(Q,element,element)
    for m in T:
        if search(Q,m) is None:
            return False
    return True
#Complejidad Temporal O(S+T)
print("-------------------------------------------------------------------------------------")
T={3,1,5,2,4}
S={1,2,3}
print(S,"Es subconjunto de ",T,is_subset(T,S))
######################################################################################
