class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        x, y = rStart, cStart
        
        result.append([x, y])
        
        if rows * cols == 1:
            return result
        
        step = 0
        
        while len(result) < rows * cols:
            # 매 두 번의 방향 전환마다 step 증가
            for i in range(4):
                if i % 2 == 0:
                    step += 1
                
                dx, dy = directions[i]
                for _ in range(step):
                    x += dx
                    y += dy
                    # 격자 내부에 있을 때만 결과에 추가
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                    
                    if len(result) == rows * cols:
                        return result
                    
        return result
