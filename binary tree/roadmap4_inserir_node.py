from typing import Optional
from trees import *


# Como inserior um novo node na nossa arvore
def inserir_node(root: Optional[TreeNode], new_node: TreeNode) -> TreeNode:
    if root is None:
        return new_node
    
    if new_node is None:
        return root

    if new_node.val < root.val:
        # Tenta inserir na esquerda e atualiza o ponteiro left
        root.left = inserir_node(root.left, new_node)
    else:
        # Tenta inserir na direita e atualiza o ponteiro right
        root.right = inserir_node(root.right, new_node)

    return root



