class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottles_drunk = 0
        empty_bottles = 0
        while 1:
            bottles_drunk += numBottles 
            empty_bottles += numBottles
            numBottles = 0
            if empty_bottles < numExchange:
                return bottles_drunk
            else:
                numBottles += 1
                empty_bottles -= (numExchange)
                numExchange += 1

