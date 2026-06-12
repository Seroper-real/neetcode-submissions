class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxL, maxR = 0, -1
        maxArea = 0
        for i in range(len(heights)):
            popped = False
            while stack and heights[i] < heights[stack[-1][1]]:
                popped = True
                l, idx = stack.pop()
                maxR = max(maxR,idx)
                area = heights[idx] * (maxR - l + 1)
                #print(f"area:{area}, idx:{idx}, maxR:{maxR}, l:{l}")
                maxArea = max(maxArea,area)
                maxL = l
            if stack and not popped and heights[i] > heights[stack[-1][1]]: maxL = i
            stack.append((maxL,i))
            maxR = -1
        maxR = -1
        while stack:
            l, idx = stack.pop()
            maxR = max(maxR,idx)
            area = heights[idx] * (maxR - l + 1)
            #print(f"area:{area}, idx:{idx}, maxR:{maxR}, l:{l}")
            maxArea = max(maxArea,area)
        return maxArea