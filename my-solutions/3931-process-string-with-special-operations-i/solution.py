class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for i in s:
            if i not in '*#%':
                result.append(i)
            elif i == '*':
                if result:
                    result.pop()
            
            elif i == '#':
                result = result + result
            elif i == '%':
                result = result[::-1]

        
        return ''.join(result)
