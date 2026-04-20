class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Balanceada
#        4
#      /   \
#     2      6
#    / \   / \
#   1   3 5   7
t1 = TreeNode(4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(6, TreeNode(5), TreeNode(7))
)


# 2. Nó único (só raiz)
#    1
t2 = TreeNode(1)


# 3. Lista encadeada (só filhos esquerdos)
#    1
#   /
#  2
# /
#3
#/
#4
t3 = TreeNode(1,
    TreeNode(2,
        TreeNode(3,
            TreeNode(4)
        )
    )
)


# 4. Assimétrica / desbalanceada
#       5
#      / \
#     3   8
#    /     \
#   2       9
#            \
#            10
t4 = TreeNode(5,
    TreeNode(3, TreeNode(2)),
    TreeNode(8, None,
        TreeNode(9, None, TreeNode(10))
    )
)


# 5. Árvore com valores negativos e None intercalados
#        0
#       / \
#     -5   3
#     /   / \
#   -8   1   7
t5 = TreeNode(0,
    TreeNode(-5, TreeNode(-8)),
    TreeNode(3, TreeNode(1), TreeNode(7))
)


# Árvore A — viola limite ancestral (erro sutil)
#        4
#       / \
#      2   6
#       \
#        5   ← INVÁLIDO: 5 > 4, não pode estar na subárvore esquerda
t_errada_a = TreeNode(4,
    TreeNode(2, None, TreeNode(5)),
    TreeNode(6)
)

# Árvore B — filho direito menor que o pai
#        4
#       / \
#      2   6
#         /
#        3   ← INVÁLIDO: 3 < 6, mas também 3 < 4, viola o limite do avô
t_errada_b = TreeNode(4,
    TreeNode(2),
    TreeNode(6, TreeNode(3), None)
)



#              50
#            /    \
#          25      75
#         /  \    /  \
#        12  37  62  90
#       /  \ / \  \  / \
#       6  18 31 43 55 68 82 97
#      /\  /\    \    /\ /\
#     3  9 15 21  46 64 78 86 93 99
#    /\              \      \
#   1  4             48     88
#       \
#        5
t_deep = TreeNode(50,
    TreeNode(25,
        TreeNode(12,
            TreeNode(6,
                TreeNode(3,
                    TreeNode(1),
                    TreeNode(4,None,TreeNode(5))
                ),
                TreeNode(9)
            ),
            TreeNode(18,
                TreeNode(15),
                TreeNode(21)
            )
        ),
        TreeNode(37,
            TreeNode(31),
            TreeNode(43,
                None,
                TreeNode(46,
                    None,
                    TreeNode(48)
                )
            )
        )
    ),
    TreeNode(75,
        TreeNode(62,
            TreeNode(55),
            TreeNode(68,
                TreeNode(64),
                None
            )
        ),
        TreeNode(90,
            TreeNode(82,
                TreeNode(78),
                TreeNode(86,
                    None,
                    TreeNode(88)
                )
            ),
            TreeNode(97,
                TreeNode(93),
                TreeNode(99)
            )
        )
    )
)


array_trees = [t1,t2,t3,t4,t5, t_errada_a, t_errada_b]