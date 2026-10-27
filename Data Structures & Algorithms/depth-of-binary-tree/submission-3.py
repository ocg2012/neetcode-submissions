# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node):
    if node.left==None and node.right==None:
        return 1
    ans1=0
    ans2=0
    if node.left!=None:
        ans1=1+dfs(node.left)
    if node.right!=None:
        ans2=1+dfs(node.right)
    return max(ans1,ans2)
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
