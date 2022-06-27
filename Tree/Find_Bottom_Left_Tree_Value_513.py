# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 最简单的想法便是层次遍历
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                queue = temp
            else:
                return queue[0].val