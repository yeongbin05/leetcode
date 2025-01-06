class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # 왼쪽에서 오른쪽으로 이동하며 계산
        count = 0  # 현재까지 만난 공의 개수
        moves = 0  # 현재까지 이동 비용
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        print(moves,count,answer)
        # 오른쪽에서 왼쪽으로 이동하며 계산
        count = 0  # 현재까지 만난 공의 개수
        moves = 0  # 현재까지 이동 비용
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        print(moves,count,answer)
        return answer

