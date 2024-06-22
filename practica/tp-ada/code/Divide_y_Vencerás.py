""" Ejercicio 8
    Búsqueda de un elemento X en una lista ordenada utilizando la técnica de divide y vencerás.
    def busquedaBinaria(lista, x):
    Descripción: Implementa la función búsqueda binaria
    Entrada: lista de números ordenados de con monotonía creciente, x número.
    Salida: True si X se encuentra en la lista, False en caso contrario.
"""
def busquedaBinaria(lista, x):
    left, right = 0, len(lista) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Calcular el punto medio        
        # Comparar el elemento buscado con el elemento del medio
        if lista[mid] == x:
            return True
        elif lista[mid] < x:
            left = mid + 1  # Ajustar el puntero de inicio
        else:
            right = mid - 1  # Ajustar el puntero de fin
    
    return False  # Elemento no encontrado
"""
Ejercicio 9
Búsqueda del k-ésimo menor elemento de una lista.
def busquedaKesimo(lista, k):
Descripción: Implementa la función búsqueda del k-ésimo elemento
Entrada: lista de números, k número que representa el k-ésimo elemento en la lista si se ordena de menor a mayor.
Salida: Valor numérico que representa el k-ésimo menor elemento en la lista.
"""
