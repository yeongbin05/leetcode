class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        for i in edges[1] :
            if i in edges[0]:
                return i
