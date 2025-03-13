class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # 단어 리스트에 beginWord 추가
        words = [beginWord] + wordList  
        n = len(words)

        # 그래프 생성
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                # 두 단어의 차이가 1개 문자일 경우 연결
                if self.isOneLetterDiff(words[i], words[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # BFS 탐색 (최단 거리 찾기)
        queue = deque([(0, 1)])  # (현재 노드 인덱스, 변환 횟수)
        visited = [False] * n
        visited[0] = True  # beginWord 방문 표시

        while queue:
            node, steps = queue.popleft()
            
            if words[node] == endWord:
                return steps
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, steps + 1))

        return 0

    def isOneLetterDiff(self, word1: str, word2: str) -> bool:
        """ 두 단어의 차이가 정확히 한 글자인지 확인하는 함수 """
        count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                count += 1
                if count > 1:
                    return False
        return count == 1
