class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        words = [0] + words
        for i in range(1,n+1):
            if words[i][0] in ['a','e','i','o','u'] and words[i][-1] in ['a','e','i','o','u']:
                words[i] = words[i-1] + 1
            else:
                words[i] = words[i-1]
        ans = []
        print(words)
        
        for i,j in queries:
            ans.append(words[j+1]-words[i])
        return ans
