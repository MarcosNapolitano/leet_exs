# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: "Optional[TreeNode]", q: "Optional[TreeNode]") -> bool:

        def recursive(p,q):

            if not p and not q:
                return True

            if not p or not q:
                return False


            

            res =  p.left.val == q.left.val and p.right.val == q.right.val

            left = recursive(p.left, q.left)
            right = recursive(p.right,q.right)

            return res

        return recursive(p,q)

a,b,c = TreeNode(val=1),TreeNode(val=2),TreeNode(val=3)

a.left = b
a.right = c

d,e,f = TreeNode(val=1),TreeNode(val=2),TreeNode(val=3)

d.left = e
d.right = f

solucion = Solution()

print(solucion.isSameTree(a,d))


