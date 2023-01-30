import queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):

    def tree_to_list_bfs(self, root : TreeNode):
        """ Use BFS to generate list from tree

        Returns:
            List: Represents nodes of tree
        """
        retVal = []
        if root == None:
            return retVal

        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            retVal.append(node.val)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)

        return retVal

    def to_binary_tree(self, items: list[int]) -> TreeNode:
        """Create BT from list of values."""
        n = len(items)
        if n == 0:
            return None

        def inner(index: int = 0) -> TreeNode:
            """Closure function using recursion bo build tree"""
            if n <= index or items[index] is None:
                return None

            node = TreeNode(items[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.invert_childs(root)
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invert_childs(self, node):
        if node == None:
            return
        t = node.left
        node.left = node.right
        node.right = t

        
        



