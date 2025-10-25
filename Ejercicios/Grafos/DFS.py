# Grafo de ejemplo (no dirigido)
grafo = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2, 7],
    5: [2, 6],
    6: [3, 5],
    7: [4]
}

def dfs_recursivo(grafo, nodo_actual, visitados, recorrido):
    # 1) Si el nodo actual no fue visitado (condición para evitar bucles)
    if nodo_actual not in visitados:
        
        # a) Agregarlo al recorrido y marcarlo como visitado
        recorrido.append(nodo_actual)
        visitados.add(nodo_actual)
        
        # b) Para cada vecino del nodo actual, recorrerlo en profundidad (RECURSIÓN)
        for vecino in grafo.get(nodo_actual, []):
            dfs_recursivo(grafo, vecino, visitados, recorrido)

def dfs_principal(grafo, nodo_inicial):
    # Inicializar las estructuras
    visitados = set()
    recorrido = []
    
    # Iniciar el recorrido en el profundidad desde el nodo_inicial
    dfs_recursivo(grafo, nodo_inicial, visitados, recorrido)
    
    # 4) Mientras existan nodos sin visitar, volver a 2) (Manejo de no conexos)
    # Recorrer todos los nodos del grafo para ver si queda alguno sin visitar
    for nodo in grafo.keys():
        if nodo not in visitados:
            dfs_recursivo(grafo, nodo, visitados, recorrido) # Si hay, se inicia un nuevo recorrido
            
    return recorrido

# Ejemplo de uso con el grafo anterior:
nodo_inicio = 4
resultado_dfs = dfs_principal(grafo, nodo_inicio)
print(f"Recorrido DFS: {resultado_dfs}")