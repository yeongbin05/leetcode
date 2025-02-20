class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        dic = {}
        binary_len = len(nums[0])
        def back(idx,arr):
            if idx == binary_len:
                key = ''.join(arr)
                if key not in dic:
                    dic[key] = 1
                return

            for i in ("0","1"):
                arr.append(i)
                back(idx+1,arr)
                arr.pop()

                    
        
        back(0,[])
    
        for i in nums:
            del dic[i]

        ans = 0
        for i in dic:
            ans = i
            break
        return ans

