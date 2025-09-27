class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calculate_area(first,second,third):
            return 0.5 * abs(first[0]*second[1] + second[0]*third[1] + third[0]*first[1]
                             -first[1]*second[0] - second[1]*third[0] - third[1]*first[0])
        n = len(points)
        ans = 0
        for i in range(n-2):
            for j in range(1,n-1):
                for k in range(2,n):
                    area = calculate_area(points[i],points[j],points[k])
                    if area > ans : 
                        ans = area

        return ans
