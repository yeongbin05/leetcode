class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
#         ans = []
#         for i in box:
#             stack = []
#             for j in i[::-1]:
#                 if j == '.':
#                     stack.append(j)
#                 elif j =='#':
#                     stack.append(j)
#                     if len(stack) == 1:
#                         continue
#                     elif stack[-2] != '#' and stack[-2] != '*':
#                         for k in range(len(stack)-2,-1,-1):
#                             if len(stack) > 1 and (stack[k] == '#' or stack[k] == '*'):
#                                 stack[k+1],stack[-1] = stack[-1],stack[k+1]
#                                 break
#                             elif len(stack) > 1 and k == 0:
#                                 stack[k],stack[-1] = stack[-1],stack[k]
#                                 break
#                 else :
#                     stack.append(j)
#             ans.append(stack[::-1])
#         ans = list(zip(*ans[::-1]))
#         return ans
        for row in box:
            empty_idx = len(row) - 1  # 오른쪽 끝부터 빈 공간을 추적
            for col in range(len(row) - 1, -1, -1):  # 뒤에서부터 탐색
                if row[col] == '#':  # 돌멩이를 만났을 때
                    row[col], row[empty_idx] = row[empty_idx], row[col]  # 빈 공간으로 이동
                    empty_idx -= 1  # 빈 공간의 위치를 앞으로 이동
                elif row[col] == '*':  # 장애물일 경우
                    empty_idx = col - 1  # 장애물 앞부터 빈 공간을 다시 탐색
    
        # 박스를 시계 방향으로 90도 회전
        rotated_box = list(zip(*box[::-1]))
        return [list(row) for row in rotated_box]
