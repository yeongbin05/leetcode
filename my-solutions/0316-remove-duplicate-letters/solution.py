class Solution(object):
    def removeDuplicateLetters(self, s):
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()  # 스택에 이미 추가된 문자를 추적합니다.
        
        for i, char in enumerate(s):
            # 이미 스택에 있는 문자는 건너뜁니다.
            if char in seen:
                continue
            
            # 스택의 마지막 문자가 현재 문자보다 사전적으로 크고,
            # 나중에 다시 등장할 수 있다면 스택에서 제거합니다.
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            # 현재 문자를 스택에 추가하고, seen에 추가합니다.
            stack.append(char)
            seen.add(char)
        
        # 스택에 있는 문자들을 이어 붙여 결과를 반환합니다.
        return ''.join(stack)
