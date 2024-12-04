class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i,j = 0,0
        while 1:
            
            if str1[i] == str2[j] or ord(str1[i]) + 1 == ord(str2[j]) or (str1[i] == 'z' and ord(str1[i]) - 25 == ord(str2[j])):

                i += 1
                j += 1

            else :
                i += 1
            if j >= len(str2) :
                return True
                
            elif i >= len(str1) :
                return False

        
