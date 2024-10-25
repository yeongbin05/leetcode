class Solution:
    def removeSubfolders(self, folder):
        # 1. 폴더를 사전 순으로 정렬
        folder.sort()
        
        # 2. 결과를 저장할 리스트
        result = []
        
        # 3. 폴더를 순회하면서 하위 폴더인지 체크
        for f in folder:
            # 결과가 비어 있거나, 현재 폴더가 마지막 결과 폴더의 하위 폴더가 아니면 추가
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result
