from dictionary import *

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

""" Ejercicio 5
    Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus
    elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución
    propuesta.
"""
def list_unico(list):
    return

""" Ejercicio 6
    Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter
    (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que
    representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e
    implementar una función de hash apropiada para los códigos postales argentinos.
"""
def cod_postal(list):
        return
""" Ejercicio 7
    Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el
    recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en
    ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su
    método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras
    mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.
"""
def list_comprimida(list):
    return