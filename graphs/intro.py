"""
Um grafo é uma estrutura de dados composta por nós (vértices) e conexões entre eles (arestas).
Ao contrário de árvores, grafos podem ter ciclos, múltiplos caminhos entre nós,
e até nós sem nenhuma conexão.

Propriedades que definem um grafo:

- Direcionado (dígrafo): as arestas têm sentido. A → B não implica B → A.
- Não-direcionado: a conexão é simétrica. Se A conecta B, B conecta A.
- Ponderado: cada aresta tem um peso (distância, custo, etc.).
- Cíclico: existe pelo menos um caminho que volta ao nó de origem.
- Acíclico: não existem ciclos. Um DAG (Directed Acyclic Graph) é o caso mais comum.
- Conexo: existe um caminho entre qualquer par de nós.
- Desconexo: alguns nós são inacessíveis a partir de outros.
"""




# ── Grafo: grade 4×3 (12 nós) ───────────────────────────────────────────────────────────
#
#   0 --- 1 --- 2 --- 3
#   |     |     |     |
#   4 --- 5 --- 6 --- 7
#   |     |     |     |
#   8 --- 9 ---10 ---11
#
#   Cada nó conecta com seus vizinhos horizontais e verticais.

grafo = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
]


from typing import List

def busca_profundidade(grafo:List[List[int]], nodo_inicio:int):
    """
    grafo: É a nossa extrutura em si (uma matriz)
    nodo_inicio: Trata-se do nó onde iniciamos nossa caminhada (linha da matriz)
    """
    visited = set()

    def dfs(nodo_atual):
        if nodo_atual in visited:
            return

        visited.add(nodo_atual)
        print("Nó atual:", nodo_atual)
        for nodo_vizinho in range(len(grafo)):
            if grafo[nodo_atual][nodo_vizinho] != 0:
                dfs(nodo_vizinho)
        
        return

    dfs(nodo_inicio)



from collections import deque

def busca_largura(grafo:List[List[int]], nodo_inicio:int):
    visited = set([nodo_inicio])
    fila = deque([nodo_inicio])

    while fila: 
        nodo_atual = fila.popleft()
        print("Nó atual:", nodo_atual)

        for nodo_vizinho in range(len(grafo)):
            if grafo[nodo_atual][nodo_vizinho] != 0 and nodo_vizinho not in visited:
                visited.add(nodo_vizinho)
                fila.append(nodo_vizinho)
        
