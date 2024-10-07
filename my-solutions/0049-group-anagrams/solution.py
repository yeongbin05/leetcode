class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        cnt = 1
        ans = []
        for i in strs:
            sort_i = ''
            for j in sorted(i):
                sort_i += j

            if sort_i in dic:
                dic[sort_i].append(i)
            else:
                dic[sort_i] = [i]

        for i in dic:
            print(dic[i],'dici')
            ans += [dic[i]]

        return ans
