class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0] * n
        ans = True
        for i in range(n):
            if i == n - 1:
                if derived[i] == 1 :
                    if original[i] != original[0]:
                        break
                    else:
                        return False

                else :
                    if original[i] == original[0]:
                        break
                    else:
                        return False




            if derived[i] == 1 :
                if original[i] == 1:
                    original[i+1] = 0
                else:
                    original[i+1] = 1

            else :
                if original[i] == 0:
                    original[i+1] = 0

                else:
                    original[i+1] = 1
        return ans
