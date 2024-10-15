class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i in ['(','{','['] :
                stack.append(i)

            else :
                if not stack :
                    return False
                elif i == ')' :
                    if stack[-1] == '(' :
                        stack.pop()
                        continue
                    else :
                        return False

                elif i == '}':
                    if stack[-1] == '{' :
                        stack.pop()
                        continue
                    else :
                        return False

                else :
                    if stack[-1] == '[' :
                        stack.pop()
                        continue
                    else :
                        return False
        if stack:
            return False
        else:
            return True
