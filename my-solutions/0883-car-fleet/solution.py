class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n < 2:
            return n
        stack = sorted(list(zip(position,speed)),reverse=True)
        stack = [(target-start)/speed for start,speed in stack]
        ans = n
        start,end = 0, 1
        while 1:
            if stack[end] <= stack[start]:
                ans -= 1
                end += 1
            else:
                start = end
                end = start + 1
            
            if start >= n or end>= n :
                break
        return ans
