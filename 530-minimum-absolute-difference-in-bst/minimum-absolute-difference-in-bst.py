# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = [float(inf)]
        prev_node = [None]
        def dfs(root):
            if root is None: return
            dfs(root.left)
            if prev_node[0] is not None:
                min_diff[0] = min(min_diff[0], (root.val - prev_node[0]))
            prev_node[0] = root.val
            dfs(root.right)
        dfs(root)
        return min_diff[0]

        