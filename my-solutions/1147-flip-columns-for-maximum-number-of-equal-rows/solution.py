class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        pattern_count = {}

        for row in matrix:
            # 행을 정규화
            normalized = tuple(val ^ row[0] for val in row)
            
            # 정규화된 패턴의 빈도를 증가
            if normalized in pattern_count:
                pattern_count[normalized] += 1
            else:
                pattern_count[normalized] = 1

        # 가장 많이 등장한 패턴의 개수를 반환
        return max(pattern_count.values())
