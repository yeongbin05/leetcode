class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        arr = [[i] for i in names]
        for i in range(len(names)) :
            arr[i].append(heights[i])
        
        arr.sort(key=lambda x:-x[1])
        res = []
        for i in arr :
            res.append(i[0])
        print(res)
        return res
