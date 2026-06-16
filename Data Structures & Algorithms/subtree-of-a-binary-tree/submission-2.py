# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not Root and not subRoot:
            return False

        if isSameTree(Root,subRoot):
            return True


        return (self.isSubtree(Root.left,subRoot) or self.isSubtree(root.right,subRoot)) 
    def isSameTree(self,p,q):
        if not p and not q:
            return True

        if p or q or p.val == q.val:
            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        
        return False










        