from solution import  Solution
from binary_tree import BinaryTree

BTree = BinaryTree()
s = Solution()

input = root = [3,9,20,None,None,15,7]
expected_output = True
# make binary tree from input
root = BTree.to_binary_tree(input)

assert s.isBalanced(root) == expected_output


input = [1,2,2,3,3,None,None,4,4]
expected_output = False
# make binary tree from input
root = BTree.to_binary_tree(input)

assert s.isBalanced(root) == expected_output


input = []
expected_output = True
# make binary tree from input
root = BTree.to_binary_tree(input)

assert s.isBalanced(root) == expected_output

print('Testing finished')
