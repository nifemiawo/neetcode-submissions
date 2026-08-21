/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        // if (root == null){
        //     return null;
        // }

        List<Integer> nodes = new ArrayList<>();
        traverse(nodes,root);
        return nodes;
        
    }
    private void traverse(List<Integer> nodes, TreeNode root){

        if (root == null){
            return ;
        }
        traverse(nodes,root.left);
        nodes.add(root.val);
        traverse(nodes,root.right);
    }
}