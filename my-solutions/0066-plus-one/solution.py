class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_digit = len(digits)
        idx = len_digit - 1
        for _ in range(len_digit):
            if digits[idx] != 9 :
                digits[idx] += 1
                break

            else:
                digits[idx] = 0
                idx -= 1

        if digits[0] == 0:
            digits = [1] + digits
        
        
        
        return digits
