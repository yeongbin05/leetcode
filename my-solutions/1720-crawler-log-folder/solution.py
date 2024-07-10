class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        ans = 0
        for i in logs:
            if i[0] == "." and i[1] == "." :
                if ans > 0 :
                    ans -=1
            elif i[0] == "." :
                continue
            else :
                ans += 1
        return ans
