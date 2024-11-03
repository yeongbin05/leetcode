from collections import deque
class Solution(object):
    def rotateString(self, s, goal):
        # s = deque(s)
        # for i in range(len(s)):
        #     if s == deque(goal):
        #         return True

        #     else :
        #         s.append(s.popleft())
        #         print(s)
        # return False
        if len(s) != len(goal):
            return False
        # s + s 안에 goal이 있는지 확인
        return goal in (s + s)
