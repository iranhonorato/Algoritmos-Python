import heapq
from grafos import g6

def djikstra(grafo, origem):

    # Armazenar pesos
    pesos = {origem: 0}

    # Armazenar nodos visitados
    visitados = set()

    # Manipulação durante execução
    heap = [(0, origem)]

    while heap:
        # Tira o nodo da heap e trabalha com seu peso e posição
        (peso, nodo_atual) = heapq.heappop(heap)

        if nodo_atual in visitados:
            continue

        visitados.add(nodo_atual)

        for nodo_vizinho in range(len(grafo)):
            novo_peso = grafo[nodo_atual][nodo_vizinho]

            if novo_peso == float("inf"):
                continue

            peso_atualizado = peso + novo_peso
            if peso_atualizado < pesos.get(nodo_vizinho, float("inf")):
                pesos[nodo_vizinho] = peso_atualizado
                heapq.heappush(heap, (peso_atualizado, nodo_vizinho))

    return pesos





print(djikstra(g6, 0))
