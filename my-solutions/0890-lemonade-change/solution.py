class Solution(object):
    def lemonadeChange(self, bills):
        change = {
            5:0,
            10:0,
            20:0,
        }
        for i in bills :

            if i == 5 :
                change[5] += 1
            elif i == 10 :
                if change[5]:
                    change[5] -= 1
                    change[10] += 1 

                else :
                    return False
            elif i == 20 :
                if change[10] >=1 and change[5] >= 1 :
                    change[10] -= 1 
                    change[5] -= 1
                    change[20] += 1
                elif change[5] >= 3 :
                    change[5] -= 3
                    change[20] += 1
                else :
                    return False

        return True
