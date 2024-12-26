class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {0:1,}
        for num in nums:
            temp = {}
            for key,value in dic.items():
                if num + key in temp:
                    temp[num+key] += value
                else:
                    temp[num+key] = value

                if key-num in temp:
                    temp[key-num] += value

                else :
                    temp[key-num] = value

            dic = temp
            print(dic)
        if target in dic:
            return dic[target]
        else:
            return 0
