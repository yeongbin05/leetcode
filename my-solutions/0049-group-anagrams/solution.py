class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        for word in strs:
            sorted_word =  ''.join(sorted(word))
            print(word)
            if sorted_word in dic:
                dic[sorted_word].append(word)
            else:
                dic[sorted_word] = [word]
            
        for i in dic:
            ans.append(dic[i])

        return ans
