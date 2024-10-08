from collections import deque
class Solution(object):
    def minSwaps(self, s):
        res=0
        numopen= 0
        for b in s:
            if b=='[':
                numopen+=1
            elif not numopen:
                numopen+=1
                res+=1
            else:
                numopen-=1
        return res
