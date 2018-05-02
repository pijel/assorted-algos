# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global traversal
        inorderTraversal(root)
        solution = [x for x in traversal if x]
        traversal = []
        return solution
traversal = []

def inorderTraversal(root):
    global traversal 
    if root:
        
        traversal.append(inorderTraversal(root.left))
        
        traversal.append(root.val)
        
        traversal.append(inorderTraversal(root.right))