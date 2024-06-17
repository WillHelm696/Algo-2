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
    while edge:
        vertex=edge.data
        add_list(graph,vertex[0],vertex[1])
        add_list(graph,vertex[1],vertex[0])
        edge = edge.next
    return graph
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
def Path(Grafo,v1,v2,visitado):
    for node in Grafo:
        current=node.head
        if current.data == v1:
            if v1 == v2:
                return True
            visitado.append(v1)
            while current.next:
                current=current.next
                if not current.data in visitado:
                    if Path(Grafo,current.data,v2,visitado):
                        return True
    return False

def existPath(Grafo,v1,v2):
    return Path(Grafo,v1,v2,[])

""" Ejercicio 3
    Implementar la función que responde a la siguiente especificación.
    def isConnected(Grafo):
    Descripción: Implementa la operación es conexo
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si existe camino entre todo par de vértices,
    False en caso contrario.
"""
def Conencted(Grafo,visitados):
    for node in Grafo:
        current=node.head
        if current.data == visitados[-1]:
            while current:
                if not current.data in visitados:
                    visitados.append(current.data)
                    Conencted(Grafo,visitados)
                current = current.next
    if len(visitados) == len(Grafo):
        return True
    return False

def isConnected(Grafo):
    if len(Grafo) > 0:
        return Conencted(Grafo,[Grafo[0].head.data])
    return False

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
    n=len(Grafo)
    for nodo in Grafo:
        if nodo.length() != n:
            return False
    return True
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
def convertToBFSTree(Grafo,v):
    Tree=[LinkedList() for _ in range(len(Grafo))]
    visitado = [False]*len(Grafo)
    queue = deque([v])
    visitado[v] = True
    while queue:
        
    return Tree
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

def display_graph(graph):
    for nodo in graph:
        current = nodo.head
        print(f"Vertice {current.data}: ",end='')
        current = current.next
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")
