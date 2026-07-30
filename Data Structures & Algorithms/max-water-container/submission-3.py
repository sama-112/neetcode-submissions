class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0 
        for i in range(len(heights)):
            for j in range(len(heights)):
                hgt = min(heights[i], heights[j])
                lngth = abs(i-j)
                if max < (hgt*lngth):
                    max = hgt*lngth
        return max
        