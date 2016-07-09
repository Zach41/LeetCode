#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        res = ""
        if self.left:
            res += str(self.left)
        res += str(self.val)
        if self.right:
            res += str(self.right)
        return res

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        index = inorder.index(postorder[-1])
        del postorder[-1]
        root = TreeNode(inorder[index])
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left  = self.buildTree(inorder[:index], postorder)

        return root

s = Solution()
import pdb
pdb.set_trace()
root = s.buildTree([4, 2, 5, 1, 6, 3], [4, 5, 2, 6, 3, 1])
print str(root)

