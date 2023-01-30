from solution import  Solution, TreeNode, BinaryTree


BTree = BinaryTree()
s = Solution()

input = [4,2,7,1,3,6,9]
expected_output = [4,7,2,9,6,3,1]
# make binary tree from input
root = BTree.to_binary_tree(input)
root = s.invertTree(root)

assert BTree.tree_to_list_bfs(root) == expected_output


input = [2,1,3]
expected_output = [2,3,1]
# make binary tree from input
root = BTree.to_binary_tree(input)
root = s.invertTree(root)

assert BTree.tree_to_list_bfs(root) == expected_output

print('Testing finished')
