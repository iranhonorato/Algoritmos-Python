from intro import g1, g2, g3, g4, g5




def verifica_ciclo_grafo_nao_direcionado(grafo):
    visited = set()

    def dfs(nodo_atual, vizinho_anterior):
        if nodo_atual in visited:
            return False
        
        visited.add(nodo_atual)
        for nodo_vizinho in range(len(grafo)):
            if grafo[nodo_atual][nodo_vizinho] == 0:
                continue

            if nodo_vizinho not in visited:
                if dfs(nodo_vizinho, nodo_atual):
                    return True # Propagar ess resultado à pilha 
            
            elif nodo_vizinho != vizinho_anterior:
                return True
        
        return False
    
    for nodo_inicial in range(len(grafo)):
        if nodo_inicial not in visited:
            if dfs(nodo_inicial, -1):
                return True

    return False





def verifica_ciclo_grafo_direcionado(grafo):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for vizinho in range(len(grafo)):
            if grafo[node][vizinho] == 0:
                continue

            if vizinho not in visited:
                if dfs(vizinho):
                    return True

            elif vizinho in rec_stack:  # aresta de retorno → ciclo
                return True

        rec_stack.remove(node)  # saindo deste caminho
        return False

    for no_inicial in range(len(grafo)):
        if no_inicial not in visited:
            if dfs(no_inicial):
                return True

    return False


