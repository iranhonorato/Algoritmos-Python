from collections import deque

queue = deque() 

# Inserindo elementos na nossa queue 

queue.append(1)
queue.append(2)
queue.append(3)
print("Nossa fila após adicionar 3 elementos ", queue, "\n")
print("Removendo o primeiro elemento da fila: ", queue.popleft())
print("Fila após remover o primeiro elemento: ", queue)
print("Removendo o segundo elemento da fila: ", queue.popright())