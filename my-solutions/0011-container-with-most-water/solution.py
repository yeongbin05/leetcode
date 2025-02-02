class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left , right = 0,n-1
        ans = 0
        while right > left :
            area = min(height[right],height[left]) * (right - left)
            if area > ans :
                ans = area

            if height[right] > height[left] : 
                left += 1
            
            else :
                right -= 1

        return ans
