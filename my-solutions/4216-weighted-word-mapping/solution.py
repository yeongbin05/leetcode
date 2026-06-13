class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            temp  = 0
            for i in word:
                temp += (weights[ord(i)-97])

            ans.append(chr(ord('z') - (temp % 26)))
    


        return ''.join(ans)
