# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans =[]
        self.traverse(root,ans)
        return ans
    
    def traverse(self,node,ans):
        if node is None:
            return
        
        self.traverse(node.left,ans)
        self.traverse(node.right,ans)
        ans.append(node.val)