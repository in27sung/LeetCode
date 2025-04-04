# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Returns (max_depth, LCA_node) for the current subtree
        def dfs(node):
            if not node:
                return 0, None  # No depth, no node

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_lca  # Deeper on the left
            elif right_depth > left_depth:
                return right_depth + 1, right_lca  # Deeper on the right
            else:
                return left_depth + 1, node  # Equal depth → current node is LCA

        return dfs(root)[1]
