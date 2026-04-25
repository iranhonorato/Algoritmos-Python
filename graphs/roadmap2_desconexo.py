from grafos import g1, g2, g3, g4, g5


def verifica_componentes_conexas(grafo):
    if not grafo:
        return True
    
    visited = set()

    def dfs(nodo_atual):
        if nodo_atual in visited:
            return 
        
        visited.add(nodo_atual)
        for nodo_vizinho in range(len(grafo)):
            if grafo[nodo_atual][nodo_vizinho] == 1:
                dfs(nodo_vizinho)
        return
    
    dfs(0)

    return len(visited) == len(grafo)


from collections import deque
def verifica_componentes_conexas_bfs(grafo):
    if not grafo:
        return True
    
    visited = set([0])
    fila = deque([0])

    while fila:
        nodo_atual = fila.popleft()
        for nodo_vizinho in range(len(grafo)):
            if grafo[nodo_atual][nodo_vizinho] == 1:
                if nodo_vizinho not in visited:
                    fila.append(nodo_vizinho)
                    visited.add(nodo_vizinho)

    return len(visited) == len(grafo)


lista = [g1,g2,g3,g4,g5]

for idx in range(len(lista)):
    print(f"O grafo {idx+1} possui apenas componentes conexas? {verifica_componentes_conexas_bfs(lista[idx])}")
