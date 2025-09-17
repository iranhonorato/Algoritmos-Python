grafo = {
    "a":["b", "e"],
    "b":["f"],
    "c":["a", "e"],
    "d":[],
    "e":["b", "d", "g"],
    "f":["e"],
    "g":["h"],
    "h":["j", "d"],
    "i":["h"],
    "j":["i"]
}


def breadth_first_search(grafo:dict, inicio:str, objetivo:str):
    queue = [] 
    verifica = None  
    closed = []
    count = 0 
    if inicio in grafo:        
        while inicio != objetivo:
            count += 1 
            for estado in grafo[inicio]:
                if estado not in closed:
                    queue.append(estado)
            verifica = inicio
            closed.append(verifica)
            verifica = queue[0]
            del queue[0]
            inicio = verifica
        if verifica == objetivo:
            return f"Encontrou na {count} Tentativas"
    else:
        return "O ponto de partida não pertence ao grafo"


print(breadth_first_search(grafo, "a", "i"))
