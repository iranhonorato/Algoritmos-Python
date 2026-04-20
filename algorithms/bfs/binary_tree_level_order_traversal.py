import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Nível 3 (Folhas)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Nível 2
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)

# Nível 1 (Raiz)
root = TreeNode(1, node2, node3)


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    fila = collections.deque()
    fila.append(root)

    while fila:
        tam = len(fila)
        level = [] # para cada nível distinto

        for i in range(tam): # dentro do mesmo nível
            node = fila.popleft()
            if node:
                level.append(node.val)
                if node.left:
                    fila.append(node.left)
                if node.right:
                    fila.append(node.right)
        if len(level) != 0:
            res.append(level)
    return res 


print(levelOrder(root))