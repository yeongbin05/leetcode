import heapq

class NumberContainers:

    def __init__(self):
        self.idx = {}  # index -> number 매핑
        self.num = {}  # number -> min-heap of indices 매핑
        self.valid = {}  # number -> 유효한 인덱스 저장 (set)

    def change(self, index: int, number: int) -> None:
        if index in self.idx:
            prev_number = self.idx[index]
            if prev_number in self.num:
                self.valid[prev_number].discard(index)  # 이전 숫자에서 유효성 제거
        
        self.idx[index] = number  # 새로운 숫자로 갱신
        
        if number not in self.num:
            self.num[number] = []
            self.valid[number] = set()
        
        heapq.heappush(self.num[number], index)  # 최소 힙에 추가
        self.valid[number].add(index)  # 유효한 인덱스 기록

    def find(self, number: int) -> int:
        if number not in self.num:
            return -1
        
        # 최소 힙에서 유효하지 않은 인덱스는 제거
        while self.num[number] and self.num[number][0] not in self.valid[number]:
            heapq.heappop(self.num[number])
        
        return self.num[number][0] if self.num[number] else -1

