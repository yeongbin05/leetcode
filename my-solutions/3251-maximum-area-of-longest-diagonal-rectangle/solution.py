class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for i,j in dimensions:
            if i**2 + j**2 > max_diagonal :
                max_diagonal = i**2+j**2

        for i,j in dimensions:
            if i**2 + j**2 == max_diagonal:
                if i * j > max_area:
                    max_area = i * j

        return max_area
