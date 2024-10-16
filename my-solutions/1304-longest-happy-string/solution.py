import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 우선순위 큐에 각 문자와 남은 개수를 넣음
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))

        result = []
        
        while max_heap:
            # 가장 많이 남은 문자를 가져옴
            first_count, first_char = heapq.heappop(max_heap)
            first_count = -first_count
            
            # 직전에 사용된 문자와 같은지 확인
            if len(result) >= 2 and result[-1] == first_char and result[-2] == first_char:
                # 직전에 두 번 사용된 문자가 동일하다면 다른 문자를 사용해야 함
                if not max_heap:
                    # 사용할 다른 문자가 없다면 종료
                    break
                
                # 두 번째로 많이 남은 문자를 가져옴
                second_count, second_char = heapq.heappop(max_heap)
                second_count = -second_count
                
                # 두 번째 문자를 추가
                result.append(second_char)
                second_count -= 1
                
                # 남은 개수가 있으면 다시 힙에 추가
                if second_count > 0:
                    heapq.heappush(max_heap, (-second_count, second_char))
                
                # 첫 번째 문자는 다시 힙에 추가
                heapq.heappush(max_heap, (-first_count, first_char))
            else:
                # 직전에 두 번 사용된 문자가 아니면 그대로 추가
                result.append(first_char)
                first_count -= 1
                
                # 남은 개수가 있으면 다시 힙에 추가
                if first_count > 0:
                    heapq.heappush(max_heap, (-first_count, first_char))
        
        return ''.join(result)
