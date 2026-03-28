# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        ans = []

        if not root:
            return []

        while q:
            print("entered to while")
            level = []

            n = len(q)
            print(n)

            for i in range(n):
                node =  q.popleft()
                level.append(node.val)
                print("level is", level)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            ans.append(level)
        
        return ans


