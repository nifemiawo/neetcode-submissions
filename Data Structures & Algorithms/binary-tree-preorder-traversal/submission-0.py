# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans =[]
        self.traverse(ans,root)
        return ans
    
    def traverse(self,ans,node):
        if node is None:
            return
        
        ans.append(node.val)
        self.traverse(ans,node.left)
        self.traverse(ans,node.right)

