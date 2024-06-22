from Backtracking import *
from Greedy import *
from Divide_y_Vencerás import *
print("Ejercicio____________________________________________________________________________________________________________1")# Ejercicio 1
monedas1 = [1, 2, 6, 8, 10]
cambio1 = 14
print(f"Para las monedas {monedas1} con cambio {cambio1} el minimo es: {darCambio(cambio1, monedas1)}")  # Output: 2

monedas2 = [1, 3, 11, 7, 12]
cambio2 = 20
print(f"Para las monedas {monedas2} con cambio {cambio2} el minimo es: {darCambio(cambio1, monedas1)}")  # Output: 3

print("Ejercicio____________________________________________________________________________________________________________2")# Ejercicio 2
PesoMax = 15
latas = [2, 3, 5, 7, 9]
print(f"De {latas} con pero en la mochila{PesoMax}: la cantidad de latas max es: {mochila(PesoMax, latas)}")  # Output podría ser [9, 5] o [7, 5, 3] u otra combinación óptima
print("Ejercicio____________________________________________________________________________________________________________3")# Ejercicio 3
numeros=[ 5, 1, 2, 3, 100, 20, 17, 8, 19, 21 ]
print(f"para los numeros {numeros} la mayor secuencia es: {subsecuenciaCreciente(numeros)}") #[1, 2,3 , 8, 19, 21 ].
print("Ejercicio____________________________________________________________________________________________________________4")# Ejercicio 4
numeros = [8, 6, 7, 5, 3, 10, 9]
valor = 15
print(f"Para {numeros} existe un subconjunto que de el valor {valor}: {subconjuntoSuma(numeros, valor)}")  # Output: True

numeros = [11, 6, 5, 1, 7, 13, 12]
valor = 15
print(f"Para {numeros} existe un subconjunto que de el valor {valor}: {subconjuntoSuma(numeros, valor)}")  # Output: False

print("Ejercicio____________________________________________________________________________________________________________5")# Ejercicio 5

tareas = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
inicio = 0
fin = 15
print(f"Para las {tareas} de {inicio} a {fin} la mejor selecion es: {adminActividades(tareas, inicio, fin)}")  # Output: [(1, 4), (5, 7), (8, 11), (12, 14)]
print("Ejercicio____________________________________________________________________________________________________________6")# Ejercicio 6
vector=[5,8,1,4,7,9]
print(f"Para el vector {vector} de maximo pares la suma de menor es: {buscaPares(vector)}")

print("Ejercicio____________________________________________________________________________________________________________7")# Ejercicio 7
PesoMax = 15
latas = [(2,1), (3,3), (5,5), (7,4), (9,2)]
print(f"De {latas} con pero en la mochila {PesoMax}: la cantidad de latas max es: {mochila_2(PesoMax, latas)}")  # Output podría ser [9, 5] o [7, 5, 3] u otra combinación óptima
print("Ejercicio____________________________________________________________________________________________________________8")# Ejercicio 7
# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 7
print(f"El valor {x} esta en la lista {lista}: ",busquedaBinaria(lista, x))  # Salida esperada: True
x = 2
print(f"El valor {x} esta en la lista {lista}: ",busquedaBinaria(lista, x))  # Salida esperada: True
