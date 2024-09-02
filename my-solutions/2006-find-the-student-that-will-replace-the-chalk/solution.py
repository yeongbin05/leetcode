class Solution(object):
    def chalkReplacer(self, chalk, k):
        k = k % sum(chalk)
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0 :
                return i
        
