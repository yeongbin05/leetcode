class Solution(object):
    def parseBoolExpr(self, expression):
        # stack = []
        # for i in range(len(expression)):
        #     stack.append(expression[i])
        #     temp = []
        #     if expression[i] == ')' :
        #         while stack[-1] != '(' :
        #             a = stack.pop()
        #             if a != ',' and a != ')': 
        #                 temp.append(a)
        #         print(temp,stack,11)
        #         if len(temp) == 1:
        #             if stack[-2] == '!':
        #                 if temp[-1] == 'f':
        #                     stack.append('t')
        #                     print(222222222222)
        #                 else:
        #                     stack.append(temp[-1])
        #                     print(2333333)
        #             else:
        #                 stack.pop()
        #                 stack.pop()
        #                 stack.append(temp[-1])
        #             print(temp,11111111111)
        #         else :
        #             inside = temp[0]
        #             if stack[-2] == '|':
        #                 for i in range(1,len(temp)):
        #                     if inside == 'f' and temp[i] =='f' :
        #                         inisde = 'f'
        #                     else:
        #                         inside = 't'
        #             elif stack[-2] == '&' :
        #                 for i in range(1,len(temp)):
        #                     if inside == 't' and temp[i] == 't':
        #                         inside = 't'
        #                     else :
        #                         inside = 'f'
        #             stack.append(inside)
        #         #stack[-1]이 "(" 이므로 pop
                
        #         print(stack,'stack')
        #         print(temp,'temp')
                

        stack = []
        for i in range(len(expression)):
            # 현재 문자를 스택에 추가
            stack.append(expression[i])
            temp = []
            
            # 닫는 괄호 ')'가 나왔을 때
            if expression[i] == ')':
                # 여는 괄호 '('가 나올 때까지 스택에서 값을 꺼내면서 수집
                while stack[-1] != '(':
                    a = stack.pop()
                    if a not in [',', ')']: 
                        temp.append(a)
                
                # 여는 괄호 '('를 제거
                stack.pop()
                
                # 연산자를 가져옴 ('!', '|', '&' 중 하나)
                operator = stack.pop() if stack and stack[-1] in ['!', '|', '&'] else ''
                
                # temp에는 괄호 안의 값들이 담겨 있음, 이를 역순으로 정리
                temp.reverse()
                
                # 연산자에 따라 처리
                if operator == '!':
                    # '!'는 temp에 단일 값이 있을 때 반전한다.
                    stack.append('t' if temp[0] == 'f' else 'f')
                elif operator == '|':
                    # '|'는 하나라도 't'가 있으면 't'
                    stack.append('t' if 't' in temp else 'f')
                elif operator == '&':
                    # '&'는 모든 값이 't'일 때만 't'
                    stack.append('t' if all(x == 't' for x in temp) else 'f')
                
                # 중간 과정을 디버그 출력
                # print(f"Temp: {temp}, Stack: {stack}, Operator: {operator}")
        
        # 마지막으로 스택에 남아 있는 값이 최종 결과
        if stack[-1] == 'f' :
            return False
        else:
            return True   
