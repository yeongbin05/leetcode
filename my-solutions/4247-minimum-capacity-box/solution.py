class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans_val = float('inf')
        ans = -1
        for idx,val in enumerate(capacity):
            if val>= itemSize and val < ans_val:
                ans = idx
                ans_val = val

        return ans
