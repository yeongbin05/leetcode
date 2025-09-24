class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)  # 나눠떨어지면 정수 반환

        sign = "-" if (numerator * denominator) < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)

        # 정수부
        integer_part = numerator // denominator
        remainder = numerator % denominator
        result = [sign + str(integer_part), "."]

        # 소수부
        remainder_map = {}  # remainder → index
        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                result.insert(idx, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)
