# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        ans = []
        
        if root is None:
            return ans
        queue.append(root)


        while len(queue) > 0 :
            temp = []
            size = len(queue)

            while size > 0:
                front = queue.pop(0)
                temp.append(front.val)

                if(front.left is not None):
                    queue.append(front.left)
                
                if(front.right is not None):
                    queue.append(front.right)
                
                size = size -1

            ans.append(temp)

        return ans
            

        