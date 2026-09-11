class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        frequency = {}

        for digit in digits:
            frequency[digit] = frequency.get(digit, 0) + 1

        ans = 0

        for first in frequency:
            if first == 0:
                continue

            frequency[first] -= 1

            for second in frequency:
                if frequency[second] == 0:
                    continue

                frequency[second] -= 1

                for last in frequency:
                    if last % 2 == 1:
                        continue

                    if frequency[last] == 0:
                        continue

                    ans += 1

                frequency[second] += 1

            frequency[first] += 1

        return ans
