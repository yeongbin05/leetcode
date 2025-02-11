class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        len_p = len(part)
        for i in s:
            stack.append(i)
            if stack[-1] == part[-1] and len(stack) >= len_p:
               
                if ''.join(stack[-len_p:]) == part :
                    for j in range(len_p):
                        stack.pop() 
        
        
        return ''.join(stack)
