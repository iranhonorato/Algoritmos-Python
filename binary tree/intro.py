
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Uma árvore binária é uma estrutura de dados hierárquica onde cada nó
tem no máximo dois filhos, chamados de filho esquerdo e filho direito.
Ela é composta por:

- Raiz: o nó do topo, sem pai
- Nós internos: têm pelo menos um filho
- Folhas: nós sem filhos (left e right são None)

É importante não confundir com árvore binária de busca (BST), que é um caso especial com uma regra a mais: 
todo nó da subárvore esquerda é menor que o pai, e todo nó da subárvore direita é maior. 

Uma árvore binária genérica não tem essa restrição — os valores podem estar em qualquer ordem.
"""



from typing import Optional

# Como percorrer uma árvore em: pré-ordem
def pre_ordem(root:Optional[TreeNode])->None:
    if root is None: 
        return

    print("Nó atual: ", root.val)
    pre_ordem(root.left)
    pre_ordem(root.right)

    return


# Como percorrer uma árvore em: pós-ordem
def pos_ordem(root:Optional[TreeNode])->None:
    if root is None: 
        return

    pos_ordem(root.left)
    pos_ordem(root.right)
    print("Nó atual: ", root.val)

    return 


# Como percorrer uma árvore em: ordem
def ordem(root:Optional[TreeNode])->None:
    if root is None: 
        return

    ordem(root.left)
    print("Nó atual: ", root.val)
    ordem(root.right)

    return 
# 1. Balanceada
#        4
#      /   \
#     2     6
#    / \   / \
#   1   3 5   7

t1 = TreeNode(4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(6, TreeNode(5), TreeNode(7))
)

print("Percorrendo a ávore em pré-ordem")
pre_ordem(t1)
# Nó atual:  4
# Nó atual:  2
# Nó atual:  1
# Nó atual:  3
# Nó atual:  6
# Nó atual:  5
# Nó atual:  7
print("\n")

print("Percorrendo a ávore em pós-ordem")
pos_ordem(t1)
# Nó atual:  1
# Nó atual:  3
# Nó atual:  2
# Nó atual:  5
# Nó atual:  7
# Nó atual:  6
# Nó atual:  4
print("\n")

print("Percorrendo a árvore em ordem")
ordem(t1)
# Nó atual:  1
# Nó atual:  2
# Nó atual:  3
# Nó atual:  4
# Nó atual:  5
# Nó atual:  6
# Nó atual:  7