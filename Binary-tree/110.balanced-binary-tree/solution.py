

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        #print(f"{self.determineHeight(root.left)}, {}")

        if abs(self.determineHeight(root.left) - self.determineHeight(root.right)) > 1:
            return False
        
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False

        return True

    def determineHeight(self, node):
        if node == None:
            return 0
        return max(self.determineHeight(node.left), self.determineHeight(node.right)) + 1

