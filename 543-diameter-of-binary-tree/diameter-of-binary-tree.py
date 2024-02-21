# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        lt = self.diameterOfBinaryTree(root.left)
        rt = self.diameterOfBinaryTree(root.right)
        curr = self.maxDepth(root.left) + self.maxDepth(root.right)
        return max(curr, max(lt, rt))
        
    def maxDepth(self, root):
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        