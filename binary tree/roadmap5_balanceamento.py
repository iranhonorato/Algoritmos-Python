from typing import Optional, List
from roadmap4_inserir_node import inserir_node
from trees import *





# Como corrigir uma árvore BST errada e balancea-la
def rebalanceamento(root:Optional[TreeNode]):
    valores = []

    def coletar_valores(root:Optional[TreeNode], valores:List[int]):
        if root is None:
            return
        
        valores.append(root.val)
        coletar_valores(root.left, valores)
        coletar_valores(root.right, valores)

        return

    coletar_valores(root, valores)
    valores.sort()
    
    def build(valores, inicio, fim):
        if inicio > fim:
            return
        
        mid = (inicio+fim)//2 
        node_val = valores[mid]

        node = TreeNode(node_val)
        node.left = build(valores, inicio=inicio, fim=mid-1)
        node.right = build(valores, inicio=mid+1, fim=fim)

        return node
    
    inicio = 0 
    fim = len(valores) - 1
    return build(valores, inicio, fim)


teste = rebalanceamento(t3)

