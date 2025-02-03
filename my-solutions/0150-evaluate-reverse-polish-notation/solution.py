class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        expression = []
        temp = 0
        for i in tokens:
            if i in '+-*/':
                expression.append(i)
                if i == '+':
                    temp = (nums[-2]+nums[-1])
                    nums.pop()
                    nums.pop()
                    nums.append(temp)

                elif i == '-':
                    temp = (nums[-2]-nums[-1])
                    nums.pop()
                    nums.pop()
                    nums.append(temp)
                elif i == '*':
                    temp = (nums[-2]*nums[-1])
                    nums.pop()
                    nums.pop()
                    nums.append(temp)
                elif i == '/':
                    temp = int(nums[-2]/nums[-1])
                    nums.pop()
                    nums.pop()
                    nums.append(temp)
            else:
                nums.append(int(i))
            
        return nums[-1]
