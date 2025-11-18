class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        idx = 0
        while 1:
            if idx == n-1:
                return True
            if bits[idx] == 1 :
                idx += 2
            else:
                idx += 1

            
            if idx >= n:
                break
            
        return False
            


        
