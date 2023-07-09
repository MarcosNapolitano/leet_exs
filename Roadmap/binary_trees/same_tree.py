# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: "Optional[TreeNode]", q: "Optional[TreeNode]") -> bool:

        def recursive(p,q):

            if not p and not q:
                return True

            left = recursive(p.left, q.left)
            right = recursive(p.right,q.right)

            res =  p.left == q.left and p.right == q.right

            return res

        return recursive(p,q)