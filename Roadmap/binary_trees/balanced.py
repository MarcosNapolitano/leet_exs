# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: "Optional[TreeNode]") -> bool:

        res = 0

        def recursive(root):

            nonlocal res

            if not root:
                return -1

            left = recursive(root.left)
            right = recursive(root.right)

            res = max(res, abs(left-right))

            return 1+max(left,right)

        recursive(root)

        if res > 1 or res<-1:
            return False
        else:
            return True

a = Solution()

b = TreeNode(1) 
c = TreeNode(2) 

d = TreeNode(2) 
e = TreeNode(3) 
f = TreeNode(3) 
g = TreeNode(4) 
h = TreeNode(4) 

b.left = c 
b.right = d
d.right = e
e.right = h 
c.left = f 
f.left = g

print(a.isBalanced(b))
