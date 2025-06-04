class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        max_len = n - numFriends + 1
        ans = ""

        for i in range(n):
            # 끝나는 위치 j는 i부터 최대 i + max_len까지 (단, 문자열 범위 내)
            
            candidate = word[i:i+max_len]
            
            if candidate > ans:
                ans = candidate
            

        return ans
