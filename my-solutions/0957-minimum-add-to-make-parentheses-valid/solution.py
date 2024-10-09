class Solution(object):
    def minAddToMakeValid(self, s):
        left = 0
        right = 0
        for i in s:
            if i == '(' :
                left += 1
            
            else :
                if left == 0:
                    right += 1
                else :
                    left -= 1
        return left + right
