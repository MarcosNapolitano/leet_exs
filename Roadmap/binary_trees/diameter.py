# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: "Optional[TreeNode]") -> int:

        contador = 0

        def recursive(root):

            nonlocal contador

            if not root:
                return -1

            left = recursive(root.left)
            right = recursive(root.right)
 
            contador = max(contador, 2 + left + right)
            return 1 + max(left,right)


        recursive(root)

        return contador[0]


