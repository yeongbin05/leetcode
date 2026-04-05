class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position =[0,0]
        for i in moves:
            if i == 'U':
                position[1] += 1
            elif i == 'D':
                position[1] -= 1
            elif i == 'L':
                position[0] -= 1
            else:
                position[0] += 1
        

        if position [0] == 0  and position[1] == 0:
            return True
        return False
