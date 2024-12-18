class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        left = [0] * len(heights)
        right = [0] * len(heights)
        stack = []
        stack1 = []

        n = len(heights)

        #next smaller element
        for i in range(len(heights) -1 , -1 , -1): 
            while(len(stack) > 0) and heights[i] <  heights[stack[-1]]:
                stack.pop()
        
            if len(stack) == 0:
                right[i] = n
            else:
                right[i] = stack[- 1]
            stack.append(i)

        #prev smaller element
        for i in range(n): 
            while(len(stack1) > 0) and heights[i] <= heights[stack1[-1]]:
                stack1.pop()
        
            if len(stack1) == 0:
                left[i] = -1
            else:
                left[i] = stack1[-1]
            
            stack1.append(i)

        ans = -1
        temp = 0

        for i in range(0,n):
            width = right[i] - left[i] -1
            temp = heights[i] * width

            if temp > ans:
                ans = temp
        
        return ans





    




        