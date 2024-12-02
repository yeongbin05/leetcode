class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        cnt = 1
        for i in sentence.split():
            if i.startswith(searchWord):
                return cnt
            
            cnt += 1

        return -1
