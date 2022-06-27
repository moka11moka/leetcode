class Solution:
    # 1. 可以层序遍历，即BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        ans = 0
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            ans += 1
        return ans
    
