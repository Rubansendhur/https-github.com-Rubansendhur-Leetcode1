# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0
        q = deque([root])
        ans = []

        if not root:
            return 0

        while q:
            print("entered while")
            level = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                level.append([node.val])
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        print(ans)
        
        return len(ans)
                
