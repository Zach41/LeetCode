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
    # Memory execeeds. 
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder  = inorder
        return self._build(0, len(preorder)-1, 0, len(inorder)-1)

    def _build(self, lp, rp, li, ri):
        if lp > rp:
            return None

        root = TreeNode(self.preorder[lp])

        for ki in range(li, ri+1):
            if self.preorder[lp] == self.inorder[ki]:
                root.left = self._build(lp+1, lp+ki-li, li, ki-1)
                root.right = self._build(lp+ki-li+1, rp, ki+1, ri)
        return root

    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder[0])
            del preorder[0]
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root

s = Solution()
import pdb
pdb.set_trace()
root = s.buildTree([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3])
print str(root)

root = s.buildTree([1], [1])
print str(root)
