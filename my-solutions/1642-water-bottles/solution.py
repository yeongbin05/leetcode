class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = numBottles
        while numBottles >= numExchange :
            ans += numBottles//numExchange
            numBottles = numBottles//numExchange + numBottles%numExchange

        return ans

