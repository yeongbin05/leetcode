class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = len(str(n))
        powers = []
        temp = 1
        while 1 :
            if len(str(temp)) <= length:
                powers.append(str(temp))
                temp = temp * 2

            else:
                break
        
        # print(powers)
        for i in powers:
            # print(sorted(i),n,str(n),sorted(str(n)))
            if sorted(i) == sorted(str(n)):
                return True
        
        return False

