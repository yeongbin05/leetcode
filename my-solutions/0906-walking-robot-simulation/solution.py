class Solution(object):
    def robotSim(self, commands, obstacles):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 장애물을 set으로 저장
        obstacle_set = set(map(tuple, obstacles))
        
        # 초기 위치 및 방향
        x, y = 0, 0
        direction = 0  # 초기 방향은 북쪽
        max_distance_sq = 0
        
        for command in commands:
            if command == -2:  # 왼쪽으로 회전
                direction = (direction - 1) % 4
            elif command == -1:  # 오른쪽으로 회전
                direction = (direction + 1) % 4
            else:  # 앞으로 이동
                for _ in range(command):
                    # 이동할 다음 위치
                    nx, ny = x + directions[direction][0], y + directions[direction][1]
                    
                    # 장애물에 부딪히면 멈춤
                    if (nx, ny) in obstacle_set:
                        break
                    
                    # 위치 업데이트
                    x, y = nx, ny
                    
                    # 거리의 제곱 계산 및 최대값 갱신
                    max_distance_sq = max(max_distance_sq, x*x + y*y)
        
        return max_distance_sq
