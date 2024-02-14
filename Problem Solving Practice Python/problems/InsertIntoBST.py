'''
701. Insert into a Binary Search Tree
Solved
Medium
Topics
Companies
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
'''


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val = val)
        if root is None:
            return node
        else:
            current = root
            while current is not None:
                if val > current.val:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
                else: 
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
        return root