class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        temp = []
        for i in triplets:
            if (i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2]) and (i[0] == target[0] or i[1] == target[1] or i[2] == target[2]):
                temp.append(i)
        print(temp)
        ans = [0] * 3
        for i in temp:
            if i[0] == target[0]:
                ans[0] = 1
            if i[1] == target[1]:
                ans[1] = 1
            
            if i[2] == target[2]:
                ans[2] = 1

        if sum(ans) == 3:
            return True

        else:
            return False
        

