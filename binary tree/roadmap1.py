from typing import Optional
from trees import *

# Como validar se a nossa árvore é ou não uma BST
def valida_arvore(root: Optional[TreeNode], menor: int = float("-inf"), maior: int = float("+inf")) -> bool:
    if root is None: # Caso base: Se chegou até aqui então funciona
        return True

    if root.val <= menor or root.val >= maior: # Se viola a condição de árvore binária dá False 
        return False

    return (
        valida_arvore(root.left, menor=menor, maior=root.val)
        and
        valida_arvore(root.right, menor=root.val, maior=maior)
    )



# for i in range(len(array_trees)):
#     print(f"teste para a {i+1}ª árvore: {valida_arvore(array_trees[i])}")

# teste para a 1ª árvore: True
# teste para a 2ª árvore: True
# teste para a 3ª árvore: False
# teste para a 4ª árvore: True
# teste para a 5ª árvore: True
# teste para a 6ª árvore: False
# teste para a 7ª árvore: False

