from Linkedlist import *
""" Ejercicio 1
    Implementar la función crear grafo que dada una lista de vértices y una lista de aristas cree un grafo
    con la representación por Lista de Adyacencia.
    def createGraph(List, List)
    Descripción: Implementa la operación crear grafo
    Entrada: LinkedList con la lista de vértices y LinkedList con la lista
    de aristas donde por cada par de elementos representa una conexión
    entre dos vértices.
    Salida: retorna el nuevo grafo
"""
def add_list(grafo,v1,v2):
    for i in range(len(grafo)):
        current = grafo[i].head
        if current.data == v1:
            grafo[i].insert(v2)

def createGraph(vertices,edges):
    v = vertices.length()
    e = edges.length()
    graph=[LinkedList() for _ in range (v)]
    vertex=vertices.head
    for i in range(v):
        graph[i].insert(vertex.data)
        vertex = vertex.next
    edge = edges.head
    if 0 < e and e <= (1/2)*v*(v-1):
        while edge:
            vertex=edge.data
            add_list(graph,vertex[0],vertex[1])
            add_list(graph,vertex[1],vertex[0])
            edge = edge.next
        return graph
    return None
""" Ejercicio 2
    Implementar la función que responde a la siguiente especificación.
    def existPath(Grafo, v1, v2):
    Descripción: Implementa la operación existe camino que busca si existe
    un camino entre los vértices v1 y v2
    Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2
    vértices en el grafo.
    Salida: retorna True si existe camino entre v1 y v2, False en caso
    contrario.
"""
def existPath(Grafo,v1,v2):
    if v1 == v2:
        return True
    for i in (len(Grafo)):
        current=Grafo[i].head
        if current.data == v1:
            while current.next:
                current=current.next
                existPath(Grafo,current.data,v2)
    return False
""" Ejercicio 3
    Implementar la función que responde a la siguiente especificación.
    def isConnected(Grafo):
    Descripción: Implementa la operación es conexo
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si existe camino entre todo par de vértices,
    False en caso contrario.
"""
#Continuar
def Conencted(Grafo,list):
    if len(list) == len (Grafo):
        return True
    for i in (len(Grafo)):
        current=Grafo[i].head
        if current.data in list:
            while current:
                if current.data in list:
                    current=current.next
                else:
                    list.apend(current.data)
            return Conencted(Grafo,list)
    return False

def isConnected(Grafo):
    return Conencted(Grafo,[Grafo.head.data])

""" Ejercicio 4
    Implementar la función que responde a la siguiente especificación.
    def isTree(Grafo):
    Descripción: Implementa la operación es árbol
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si el grafo es un árbol.
"""
def isTree(Grafo):
    return
""" Ejercicio 5
    Implementar la función que responde a la siguiente especificación.
    def isComplete(Grafo):
    Descripción: Implementa la operación es completo
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si el grafo es completo.
    Nota: Tener en cuenta que un grafo es completo cuando existe una arista entre todo par de
    vértices.
"""
def isComplete(Grafo):
    return
""" Ejercicio 6
    Implementar una función que dado un grafo devuelva una lista de aristas que si se eliminan el grafo
    se convierte en un árbol. Respetar la siguiente especificación.
    def convertTree(Grafo)
    Descripción: Implementa la operación es convertir a árbol
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: LinkedList de las aristas que se pueden eliminar y el grafo
    resultante se convierte en un árbol.
"""
def convertTree(Grafo):
    return
"""
mplementar la función que responde a la siguiente especificación.
    def countConnections(Grafo):
    Descripción: Implementa la operación cantidad de componentes conexas
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna el número de componentes conexas que componen el
    grafo.
"""
def countConnections(Grafo):
    return
"""
    Implementar la función que responde a la siguiente especificación.
    def convertToBFSTree(Grafo, v):
    Descripción: Convierte un grafo en un árbol BFS
    Entrada: Grafo con la representación de Lista de Adyacencia, v vértice
    que representa la raíz del árbol
    Salida: Devuelve una Lista de Adyacencia con la representación BFS del
    grafo recibido usando v como raíz.
"""
def convertToBFSTree(Grafo, v):
    
    return
"""
    Implementar la función que responde a la siguiente especificación.
    def convertToDFSTree(Grafo, v):
    Descripción: Convierte un grafo en un árbol DFS
    Entrada: Grafo con la representación de Lista de Adyacencia, v vértice
    que representa la raíz del árbol
    Salida: Devuelve una Lista de Adyacencia con la representación DFS del
    grafo recibido usando v como raíz.
"""
def convertToDFSTree(Grafo, v):
    return
"""
Implementar la función que responde a la siguiente especificación.
def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre
dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2
vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más
corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al
final a v2. En caso que no exista camino se retorna la lista vacía.
"""
def bestRoad(Grafo, v1, v2):
    return
"""
    Implementar la función que responde a la siguiente especificación.
    def isBipartite(Grafo):
    Descripción: Implementa la operación es bipartito
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si el grafo es bipartito.
    NOTA: Un grafo es bipartito si no tiene ciclos de longitud impar.
"""
def isBipartite(Grafo):
    return

def display_graph(self):
    for i in range(len(self)):
        current = self[i].head
        print(f"Vertice {current.data}: ",end='')
        current = current.next
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")
