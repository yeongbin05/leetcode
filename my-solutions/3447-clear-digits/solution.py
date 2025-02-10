class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        # True -> 숫자 , False -> 문자
        flag = False
        for i in s :
            if i in '0123456789':
                flag = True
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)
