from typing import Optional, List
from trees import *
from roadmap1 import valida_arvore


# Como corrigir uma árvore BST errada e balancea-la
def coletar_valores(root:Optional[TreeNode], valores:List[int]):
    if root is None:
        return
    
    valores.append(root.val)
    coletar_valores(root.left, valores)
    coletar_valores(root.right, valores)

    return

def corrige_bst(root:Optional[TreeNode]):
    valores = []

    coletar_valores(root, valores)
    return valores


print(corrige_bst(t1))

