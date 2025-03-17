class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            if ''.join(sorted(i)) in dic:
                dic[''.join(sorted(i))].append(i)
            else:
                dic[''.join(sorted(i))] = [i]

        ans = []
        for i in dic:
            ans.append(dic[i])

        return ans
