class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key = lambda x:(x[0],x[1]))
        temp = []
        for i,j in intervals:
            if temp == []:
                temp = [i,j]
            else:
                if i <= temp[1]:
                    if j > temp[1]:
                        temp[1] = j
                    
                
                else:
                    ans.append(temp)
                    temp = [i,j]

        if temp != []:
            ans.append(temp)

        return ans
