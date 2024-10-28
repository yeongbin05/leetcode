class Solution(object):
    def longestSquareStreak(self, nums):
        # dic = {}
        # nums = list(set(nums))
        # nums.sort(reverse=True)
        # print(nums)
        # for i in nums:
        #     if i**2 in dic:
        #         dic[i] = 1
        #         while i**2 in dic:
        #             print(i)
        #             i = i ** 2
        #             print(i)
        #         dic[i] += 1

        #     else :
        #         dic[i] = 1
        # ans = 1
        # for i,j in dic.items():
        #     if j > ans:
        #         ans = j

        # if ans == 1:
        #     return -1
        
        # return ans
        num_set = set(nums)  # 중복 제거 및 빠른 조회를 위한 set
        nums = sorted(num_set)  # 오름차순 정렬
        max_streak = 0
        length_map = {}  # 각 숫자의 최대 길이를 저장

        for num in nums:
            if num in length_map:  # 이미 계산된 숫자는 무시
                continue
                
            streak_length = 0
            current = num
            
            while current in num_set:
                streak_length += 1
                length_map[current] = streak_length  # 현재 숫자에 대한 시퀀스 길이 저장
                current = current * current  # 제곱으로 다음 숫자 찾기

            if streak_length >= 2:
                max_streak = max(max_streak, streak_length)

        return max_streak if max_streak >= 2 else -1

