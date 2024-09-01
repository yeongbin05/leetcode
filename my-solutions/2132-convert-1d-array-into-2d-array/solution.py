class Solution(object):
    def construct2DArray(self, original, m, n):
        if m*n != len(original) :
            return []

        arr = []
        num = 0
        for i in range(m):
            temp = []
            for j in range(num,num+n):
                temp.append(original[j])
                num += 1
            arr.append(temp)
        return arr
