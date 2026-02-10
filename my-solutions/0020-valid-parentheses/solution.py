class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')' : '(',
            ']' : '[',
            '}' : '{',

        }
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False

                if stack.pop() == pair[i]:
                    pass
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False

