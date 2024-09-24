class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        arr1 = set(arr1)
        arr2 = set(arr2)

        dic1 = {}
        dic2 = {}

        for i in arr1:
            for j in range(1,len(str(i))+1):
                if str(i)[:j] not in dic1:
                    dic1[str(i)[:j]] = 1
        
        for i in arr2:
            for j in range(1,len(str(i))+1):
                if str(i)[:j] not in dic2:
                    dic2[str(i)[:j]] = 1

                
        for i in dic1:
            if i in dic2:
                print(11111)
                if len(i) > ans :
                    ans = len(i)
       
        print(dic1,dic2)
        return ans



