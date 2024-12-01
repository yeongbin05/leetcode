class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            dic[arr[i]] = i
        print(dic)
        for i in range(len(arr)):
            print(arr[i]*2,dic[arr[i]],i)
            if arr[i] * 2 in dic and dic[arr[i]*2] != i:
                return True
        return False
