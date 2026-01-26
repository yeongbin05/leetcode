class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        min_abs = float('inf')
        ans = []
        for i in range(n-1):
            if arr[i+1] - arr[i] < min_abs:
                min_abs = arr[i+1] - arr[i]
                ans = [[arr[i],arr[i+1]]]
            elif arr[i+1] - arr[i] == min_abs:
                ans.append([arr[i],arr[i+1]])
            
        
        return ans
