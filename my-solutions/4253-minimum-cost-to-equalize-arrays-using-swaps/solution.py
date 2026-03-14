class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        dic = {}
        dic1 = {}
        dic2 = {}
        if sorted(nums1) == sorted(nums2) :
            return 0

        for i in range(n):
            if nums1[i] in dic:
                dic[nums1[i]] += 1
            else:
                dic[nums1[i]] = 1
            if nums2[i] in dic:
                dic[nums2[i]] += 1
            else:
                dic[nums2[i]] = 1

            if nums1[i] in dic1:
                dic1[nums1[i]] += 1
            else:
                dic1[nums1[i]] = 1

            if nums2[i] in dic2:
                dic2[nums2[i]] += 1
            else:
                dic2[nums2[i]] = 1
        for i in dic:
            if dic[i] % 2 == 1:
                return -1

        ans = 0

        temp  = 0
        for i in dic1:
            if i not in dic2 :
                temp += dic1[i]
            elif dic1[i] > dic2[i]:
                temp += (dic1[i] - dic2[i])
            
        for i in dic2:
            if i not in dic1 :
                temp += dic2[i]
            elif dic2[i] > dic1[i]:
                temp += (dic2[i] - dic1[i])
            

        return temp//4
