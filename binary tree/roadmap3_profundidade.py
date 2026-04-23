from typing import Optional
from trees import *

# Como descobrir a profundidade máxima de uma árvore 
def profundidade(root:Optional[TreeNode]):
    
    def dfs(root, deep):
        if root is None:
            return deep-1

        deep += 1
        left = dfs(root.left, deep)
        right = dfs(root.right, deep)
        
        if left > right:
            return left 
        
        return right 
    
    return dfs(root, 0)


print(profundidade(t_deep))

        
        

        

