class Solution(object):
    def findTheLongestSubstring(self, s):
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        # 초기 상태 및 상태 맵 (처음 상태는 0)
        state = 0
        state_map = {0: -1}
        max_length = 0
        
        for i, char in enumerate(s):
            # 문자가 모음일 경우 상태를 갱신
            if char in vowels:
                state ^= vowels[char]
            
            # 동일한 상태가 이전에 등장한 경우
            if state in state_map:
                max_length = max(max_length, i - state_map[state])
            else:
                state_map[state] = i
        
        return max_length
