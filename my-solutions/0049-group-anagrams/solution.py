class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            cnt = [0] * 26
            for j in i:
                cnt[ord(j)-ord('a')] += 1
            
            if tuple(cnt) in dic:
                dic[tuple(cnt)].append(i)
            else:
                dic[tuple(cnt)] = [i]

        ans = []
        for i in dic:
            ans.append(dic[i])
        return ans
