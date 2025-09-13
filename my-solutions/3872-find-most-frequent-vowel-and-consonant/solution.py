class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}
        consonants = {}
        for i in s:
            if i in 'aeiou':
                if i in vowels:
                    vowels[i] += 1
                else:
                    vowels[i] = 1
        
            else:
                if i in consonants:
                    consonants[i] += 1
                else:
                    consonants[i] = 1

        max_vowels = 0
        max_consonants = 0
        for i in vowels:
            if vowels[i] > max_vowels:
                max_vowels = vowels[i]
        for i in consonants:
            if consonants[i] > max_consonants:
                max_consonants = consonants[i]


        return max_vowels + max_consonants
