class Solution:
    def minLength(self, s: str) -> int:
        while 1 :
            if 'AB' in s or 'CD' in s:
                if 'AB' in s:
                    s = s.replace('AB','')
                if 'CD' in s:
                    s = s.replace('CD','')
            else:
                break

        return len(s)        


        
