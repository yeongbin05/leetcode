class Solution(object):
    def countConsistentStrings(self, allowed, words):
        ans = 0
        dic = {}
        for i in allowed:
            if i not in dic:
                dic[i] = 1
        for i in words:
            for j in i:
                if j not in dic:
                    break
            else:
                ans += 1
        return ans
        
