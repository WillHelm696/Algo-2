from dictionary import *
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
delete(D,15)
print_dictionary(D)
""" Ejercicio 4
    Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente
    proposición: dado dos strings s1...sk y p1...pk, se quiere encontrar si los caracteres de p1...pk
    corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.
"""
def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    frecuencia = {}
    for char in list1:
        if char in frecuencia:
            frecuencia[char]+=1
        else:
            frecuencia[char]=1

    for char in list2:
        if char in frecuencia:
            frecuencia[char]-=1
        else:
            return False
    for count in frecuencia:
        if count !=0:
            return False
    return True
print("-------------------------------------------------------------------------------------")

######################################################################################
""" Ejercicio 5
    Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus
    elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución
    propuesta.
"""
def list_unico(list):
    if len(list)>0:
        S=dictionary()
        S.head=[None]*len(list)
        for n in list:
            insert(S,n,n)
        print_dictionary(S)
        for m in S.head:
            if m is None:
                return False
        return True
    return False
L=[1,5,12,3,2]
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
def list_comprimida(list):
    return