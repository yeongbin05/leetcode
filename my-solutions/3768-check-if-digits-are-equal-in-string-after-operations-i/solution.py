class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while 1 :
            temp = ''
            for i in range(len(s)-1):

                temp += str((int(s[i])+int(s[i+1]))%10)

            if len(temp) == 2:
                break
            s = temp
        
        return temp[0] == temp[1]
