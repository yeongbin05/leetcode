class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        ans = 1
        flag = True
        for i in range(time):
            if ans == n :
                flag = False
            if ans == 1:
                flag = True
            if flag == True :
                ans +=1
            else :
                ans -=1
        return ans


