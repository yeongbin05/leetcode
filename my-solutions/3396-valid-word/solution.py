class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        vowel = 0
        consonant = 0
        for i in word:
            if i.isalpha():
                if i in 'aeiouAEIOU':
                    vowel += 1
                else:
                    consonant += 1
        if vowel == 0 :
            return False
        if consonant == 0:
            return False

        return True


