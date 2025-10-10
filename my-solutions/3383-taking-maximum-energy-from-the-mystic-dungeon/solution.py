class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        for i in range(n):
            if i-k >= 0:
                energy[i] = max(energy[i],energy[i-k] + energy[i])

      
        return max(energy[n-k:])

