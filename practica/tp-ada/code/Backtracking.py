""" Ejercicio 1
    Implementar la función Dar Cambio que devuelve la cantidad mínima de monedas que hay que dar
    para cambiar n pesos con monedas de la denominación dada como parámetro.
    def darCambio(Cambio, Monedas)
    Descripción: Implementa la operación devolver cambio
    Entrada: Cambio número que representa el monto del cambio, Monedas, un
    Array con las monedas que se dispone para dar ese cambio.
    Salida: retorna el número mínimo de monedas que son utilizadas para
    devolver el cambio.
    Nota: Asuma que en la lista de monedas siempre está la moneda con valor 1. Y que las monedas no
    se agotan.
    Ejemplos:
    monedas = [1, 2, 6, 8, 10], cambio = 14, solución: 2 (una moneda con denominación 6 y otra con 8)
    monedas = [1, 3, 11, 7, 12], cambio = 20, solución: 3 (utilizando la combinación de monedas 12,7,1)
"""
def darCambio(cambio, monedas):
    # Inicializar el mejor número de monedas a un valor muy alto
    min_coins = [float('inf')]
    # Ordenar las monedas en orden descendente para optimización
    monedas.sort(reverse=True)
    def backtrack_1(remaining, count):
        # Si el cambio restante es 0, se encontró una combinación válida
        if remaining == 0:
            min_coins[0] = min(min_coins[0], count)
            return
        # Si el cambio restante es negativo, no es una combinación válida
        if remaining < 0:
            return
        # Probar cada moneda
        for coin in monedas:
            # Solo continuar si la combinación actual no excede el mejor número de monedas encontrado
            if count + 1 < min_coins[0]:
                backtrack_1(remaining - coin, count + 1)
    # Iniciar el backtracking con el cambio total y 0 monedas usadas
    backtrack_1(cambio, 0)
    # Si no se encontró ninguna combinación válida, min_coins[0] seguirá siendo float('inf')
    return min_coins[0] if min_coins[0] != float('inf') else -1
""" Ejercicio 2
    Se dispone de una mochila que acepta un peso máximo PesoMax, y de k latas de peso P1, P2, P3,
    …, Pk, todos diferentes. Se desea llevar la mayor cantidad de peso posible en la mochila. Implemente
    un método que decida que latas deben echarse con este fin.
    def mochila(PesoMax, latas):
    Descripción: Implementa la función mochila
    Entrada: PesoMax número que representa el peso máximo que acepta la
    mochila, latas Array con el peso de las latas p1, p2, p3, …, p_length_array.
    Salida: retorna un array con las latas que maximizan el peso de la
    mochila.
"""
def mochila(PesoMax, latas):
    def backtrack_2(index, current_peso, current_selection):
        # Acceso a la variable de la mejor combinación encontrada
        nonlocal best_peso, best_seleccion
        # Si el peso actual es mayor al mejor encontrado, actualizamos la mejor combinación
        if current_peso > best_peso:
            best_peso = current_peso
            best_seleccion = current_selection[:]
        # Exploramos las siguientes latas
        for i in range(index, len(latas)):
            next_peso = current_peso + latas[i]
            if next_peso <= PesoMax:
                current_selection.append(latas[i])
                backtrack_2(i + 1, next_peso, current_selection)
                current_selection.pop()
    # Inicializar variables para la mejor combinación encontrada
    best_peso = 0
    best_seleccion = []
    # Iniciar el backtracking desde el índice 0
    backtrack_2(0, 0, [])
    return best_seleccion
""" Ejercicio 3
    Implementar la función SubsecuenciaCreciente que devuelva un array con la mayor cantidad de
    elementos del array de entrada que formen una secuencia monótona creciente. Los elementos en el
    resultado deben aparecer en el mismo orden en que aparecían en el array de entrada, y no tienen que
    ser consecutivos dentro de este. Por ejemplo, la mayor subsecuencia creciente en [ 5, 1, 2, 3, 100, 20,
    17, 8, 19, 21 ] es [1, 2,3 , 8, 19, 21 ].
    def subsecuenciaCreciente(numeros):
    Descripción: Implementa la función SubsecuenciaCreciente
    Entrada: numeros array de números naturales.
    Salida: retorna array de números con la mayor subsecuencia creciente en el array de entrada numero.
    Nota: puede haber más de una respuesta, el ejercicio solo exige que usted devuelva una de ellas.
"""
def subsecuenciaCreciente(numeros):
    def backtrack(index, current_subsecuencia):
        nonlocal best_subsecuencia
        # Si la subsecuencia actual es mayor que la mejor encontrada, actualizamos la mejor
        if len(current_subsecuencia) > len(best_subsecuencia):
            best_subsecuencia = current_subsecuencia[:]
        # Explorar subsecuencias comenzando desde el índice actual
        for i in range(index, len(numeros)):
            # Solo agregar el número si es mayor que el último de la subsecuencia actual
            if not current_subsecuencia or numeros[i] > current_subsecuencia[-1]:
                current_subsecuencia.append(numeros[i])
                backtrack(i + 1, current_subsecuencia)
                current_subsecuencia.pop()
    best_subsecuencia = []
    backtrack(0, [])
    return best_subsecuencia
""" Ejercicio 4
    Dado un array X de números enteros positivos y un número entero de T, implementar un algoritmo
    que devuelva si existe un subconjunto de elementos en X que suman el valor T. Por ejemplo si X = {8,
    6, 7, 5, 3, 10, 9} y T = 15, la respuesta es True, porque los subconjuntos {8, 7} , {7, 5, 3} , {6, 9} , {5,
    10} todos suman 15. Con este otro ejemplo X = {11, 6, 5, 1, 7, 13, 12} y T = 15, la respuesta es False.
    def subconjuntoSuma(numeros, valor):
    Descripción: Implementa la función Subconjunto Suma
    Entrada: numeros array de enteros positivos, valor entero positivo.
    Salida: retorna True si existe un grupo de enteros en números cuya
    suma del valor de entrada.
"""
def subconjuntoSuma(numeros, valor):
    def backtrack(index, current_sum):
        # Si la suma actual es igual al valor objetivo, hemos encontrado un subconjunto
        if current_sum == valor:
            return True
        # Si la suma actual excede el valor objetivo o hemos considerado todos los elementos, devolver False
        if current_sum > valor or index == len(numeros):
            return False
        # Opción 1: Incluir el número actual en la suma
        if backtrack(index + 1, current_sum + numeros[index]):
            return True
        # Opción 2: Excluir el número actual de la suma
        if backtrack(index + 1, current_sum):
            return True
        return False
    return backtrack(0, 0)

