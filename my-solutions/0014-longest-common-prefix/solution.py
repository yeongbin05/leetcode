class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 예외 처리: 빈 리스트일 경우
            return ""
        
        # 1. 문자열 리스트를 사전 순으로 정렬
        strs.sort()
        
        # 2. 첫 번째와 마지막 문자열만 비교하면 충분함
        first = strs[0]
        last = strs[-1]
        
        # 3. 공통 접두사를 저장할 변수
        ans = ""
        
        # 4. 두 문자열의 각 문자를 순차적으로 비교
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        
        return ans
