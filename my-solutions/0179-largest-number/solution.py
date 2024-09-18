class Solution(object):
    def largestNumber(self, nums):
        # # 숫자를 문자열로 변환
        # nums_str = list(map(str, nums))
        
        # # 문자열을 12글자 길이로 확장하여 정렬
        # nums_str_sorted = sorted(nums_str, key=lambda x: x * 12, reverse=True)
        
        # # 모든 숫자가 '0'인 경우 '0' 반환
        # if nums_str_sorted[0] == "0":
        #     return "0"
        
        # # 정렬된 문자열을 합쳐서 결과 반환
        # return "".join(nums_str_sorted)
        def sortKey(x):
            ret = ""
            while len(ret) < 12:
                ret += x
            return ret[:12]

        sortedNums = sorted(map(str,nums), key=sortKey, reverse=True)
        if max(sortedNums) == "0":
            return "0"
        else:
            return "".join(sortedNums)
