class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        left ,right = 0, len(height) - 1
        max_left , max_right = height[left] , height[right]
        while right > left :
            if height[right] >= height[left]:
                left += 1
                max_left = max(max_left,height[left])
                ans += max_left - height[left]
            elif height[right] < height[left]:
                right -= 1
                max_right = max(max_right,height[right])
                ans += max_right - height[right]
        
        return ans
