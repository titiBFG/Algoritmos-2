from collections import deque

grafo = {
  1: [2,3],
  2: [1,4,5],
  3: [1,6],
  4: [2,7],
  5: [2,6],
  6: [3,5],
  7: [4]
}

def bfs_iterativo(grafo, nodo_inicio):
  # 1. Inicialización
  visitados = {nodo_inicio}
  cola = deque([nodo_inicio])
  recorrido = [nodo_inicio]

  # 2. Bucle principal (Mientras haya nodos en la cola)
  while cola:
      # Desencolar (FIFO)
      nodo_actual = cola.popleft() 
      
      # 3. Explorar Vecinos
      for vecino in grafo.get(nodo_actual, []):
          if vecino not in visitados:
              visitados.add(vecino)
              recorrido.append(vecino)
              # Encolar
              cola.append(vecino)
              
  return recorrido

if __name__ == "__main__":
  nodo_inicio = 1
  resultado_bfs = bfs_iterativo(grafo, nodo_inicio)
  print(f'Recorrido BFS: {resultado_bfs}')
