class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        if start.replace("_", "") != target.replace("_", ""):
            return False
        start_L = [i for i in range(n) if start[i] =='L']
        start_R = [i for i in range(n) if start[i] =='R']
        target_L = [i for i in range(n) if target[i] =='L']
        target_R = [i for i in range(n) if target[i] =='R']

        if len(start_L) != len(target_L) or len(start_R) != len(target_R) :
            return False
        for i in range(len(start_L)):
            if start_L[i] < target_L[i]:
                return False

        for i in range(len(start_R)):
            if start_R[i] > target_R[i] :
                return False

        return True
