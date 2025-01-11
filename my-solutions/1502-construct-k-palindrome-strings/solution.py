class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        # Initialize oddCount as an integer bitmask
        odd_count = 0

        # Update the bitmask for each character in the string
        for chr in s:
            odd_count ^= 1 << (ord(chr) - ord("a"))
        # Return if the number of odd frequencies is less than or equal to
        return bin(odd_count).count("1") <= k
        dic = {}
        if len(s) < k :
            return False
        if len(s) == k:
            return True
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        temp = 0
        for i in dic:
            if dic[i] % 2 != 0:
                temp += 1
        if temp > k :
            return False

        else :
            return True
