class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    ans.add(words[i])
        ans = list(ans)


        return ans
