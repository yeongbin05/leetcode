class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index,text):
            if len(text) == len(digits):
                ans.append(text)
                return

            for i in range(index,len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1,text+j)
        if not digits:
            return []
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        ans = []
        dfs
        dfs(0,"")

        return ans
