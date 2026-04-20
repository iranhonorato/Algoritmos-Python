from collections import deque

queue = deque() 
for i in range(1,11):
    queue.append(i)

deletado = queue.popleft()
print(deletado)