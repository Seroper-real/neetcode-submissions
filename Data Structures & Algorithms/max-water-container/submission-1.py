class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        lid, rid = 0, len(heights) - 1
        while lid < rid:
            area = max(area,(rid - lid) * min(heights[rid], heights[lid]))
            #print(f"comparing:{heights[lid]}, {heights[rid]}, max is: {area}")
            if heights[lid] > heights[rid]:
                rid -= 1
            else:
                lid += 1
        return area