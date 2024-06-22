""" Ejercicio 5
    N actividades requieren el uso exclusivo de un recurso común. Cada actividad dispone de un tiempo
    de inicio y fin. Seleccionar el mayor conjunto posible de actividades que no se superpongan.
    def adminActividades(tareas, inicio, fin):
    Descripción: Implementa la función Administrar tareas
    Entrada: tareas array con las tareas donde cada tarea dispone de un
    tiempo de inicio t0 y un tiempo final tf, inicio entero positivo que
    representa desde cuando esta disponible el recurso común, fin entero
    positivo que representa hasta cuando esta disponible el recurso común.
    Toda tarea esta dentro de ese tiempo.
    Salida: retorna el listado de tareas que maximiza el uso del espacio
    en común sin que se solapen ninguna de estas.
"""
def adminActividades(tareas, inicio, fin):
    # Ordenar las tareas por su tiempo de finalización
    tareas_ordenadas = sorted(tareas, key=lambda x: x[1])
    # Lista para almacenar las tareas seleccionadas
    tareas_seleccionadas = []
    # Variable para llevar el tiempo de finalización de la última tarea seleccionada
    tiempo_final_anterior = inicio
    for tarea in tareas_ordenadas:
        # Si el inicio de la tarea es mayor o igual al tiempo final de la última tarea seleccionada
        if tarea[0] >= tiempo_final_anterior and tarea[1] <= fin:
            # Seleccionamos la tarea
            tareas_seleccionadas.append(tarea)
            # Actualizamos el tiempo final de la última tarea seleccionada
            tiempo_final_anterior = tarea[1]
    return tareas_seleccionadas
""" Ejercicio 6
    Se tienen n números naturales distintos, siendo n una cantidad par, que tienen que juntarse formando
    parejas de dos números cada una. A continuación, de cada pareja se obtiene la suma de sus dos
    componentes, y de todos estos resultados se toma el máximo. Diseñar un algoritmo greedy que cree
    las parejas de manera que el valor máximo de las sumas de los números de cada pareja sea lo más
    pequeño posible. Ejemplo: suponiendo que los datos se encuentran en el siguiente vector
    [5,8,1,4,7,9]
    vamos a ver un par de formas de resolver el problema (no necesariamente la óptima):
    ● Seleccionamos como pareja los elementos consecutivos. De esta forma conseguimos las
    parejas (5, 8), (1, 4) y (7, 9); entonces, al sumar las componentes tenemos los valores 13, 5 y
    16, por lo que el resultado final es 16.
    ● Seleccionamos como pareja los elementos opuestos en el vector Ahora tenemos las parejas
    (5, 9), (8, 7) y (1, 4); sumando conseguimos 14, 15 y 5, por lo que el resultado final es 15
    (mejor que antes).
    ¿Habrá una resultado mejor para este ejemplo?
    def buscaPares(vector):
    Descripción: Implementa la función busca pares
    Entrada: vector de tamaño par que contiene números enteros positivos.
    Salida: retorna el valor mínimo de sumar los posibles pares que se
    pueden formar del vector (justo como se explica en la especificación
    anterior).
"""
def buscaPares(vector):
    # Ordenar el vector en orden ascendente
    vector.sort()
    n = len(vector)
    max_sum = 0
    # Emparejar los elementos desde los extremos hacia el centro
    for i in range(n // 2):
        current_sum = vector[i] + vector[n - 1 - i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
""" Ejercicio 7
    Se dispone de una mochila que acepta un peso máximo PesoMax, y de k latas de peso P1, P2, P3,
    …, Pk, todos diferentes. Cada lata dispone de un beneficio B1, B2, B3, …, Bk. Se desea llevar la
    mayor cantidad de beneficio posible en la mochila sin sobrepasar el peso. Implemente un método que
    decida que latas deben echarse con este fin.
    def mochila(PesoMax, latas):
    Descripción: Implementa la función mochila
    Entrada: PesoMax número que representa el peso máximo que acepta la
    mochila, latas Array con el peso de las latas p1, p2, p3, …,
    plength_array.
    Salida: retorna un array con las latas que maximizan el beneficio de
    la mochila.
    NOTA: Parecido al ejercicio 2 solo notar que en este caso se le agrega un beneficio a cada
    lata y lo que se quiere es maximizar el beneficio en total sin sobrepasar el peso de la mochila.
"""
def mochila_2(PesoMax, latas):
    # Calcular el ratio beneficio/peso para cada lata y almacenar con su peso y beneficio
    ratios = [(beneficio / peso, peso, beneficio) for peso, beneficio in latas]
    # Ordenar las latas por ratio en orden descendente
    ratios.sort(reverse=True, key=lambda x: x[0])
    peso_actual = 0
    beneficio_total = 0
    seleccionadas = []
    # Seleccionar las latas mientras no se exceda PesoMax
    for ratio, peso, beneficio in ratios:
        if peso_actual + peso <= PesoMax:
            seleccionadas.append((peso, beneficio))
            peso_actual += peso
            beneficio_total += beneficio
    return seleccionadas, beneficio_total

