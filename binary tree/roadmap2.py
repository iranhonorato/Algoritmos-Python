from typing import Optional
from trees import *


# contando todos os nós de uma árvore
def conta_nodos(root:Optional[TreeNode]):
    if root is None:
        return 0
    
    return conta_nodos(root.left) + conta_nodos(root.right) + 1


# for i in range(len(array_trees)):
#     print(f"Número de nodos para a {i+1}ª árvore: {conta_nodos(array_trees[i])}")

# Número de nodos para a 1ª árvore: 7
# Número de nodos para a 2ª árvore: 1
# Número de nodos para a 3ª árvore: 4
# Número de nodos para a 4ª árvore: 6
# Número de nodos para a 5ª árvore: 6
# Número de nodos para a 6ª árvore: 4
# Número de nodos para a 7ª árvore: 4