class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans = []
        n= len(s)
        temp = ""
        temp_len = 0
        for i in range(n):
            temp+=s[i]
            temp_len+=1
            if temp_len == k:
                ans.append(temp)
                temp_len =0
                temp=""
            
            
        if temp_len != 0:
            for j in range(k-temp_len):
                temp+=fill
            ans.append(temp)
        return ans
