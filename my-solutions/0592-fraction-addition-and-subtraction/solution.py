from math import gcd
import re
class Solution:

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        numerator, denominator = 0, 1
        
        for frac in fractions:
            num, den = map(int, frac.split('/'))
            denominator = lcm(denominator, den)
        
        for frac in fractions:
            num, den = map(int, frac.split('/'))
            numerator += num * (denominator // den)
        
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        
        if numerator == 0:
            return "0/1"
        
        return f"{numerator}/{denominator}"

