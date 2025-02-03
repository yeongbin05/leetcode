class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def back(stack, open_count, close_count):
            if len(stack) == n * 2:
                ans.append(''.join(stack))
                return
            
            if open_count < n:
                stack.append('(')
                back(stack, open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(')')
                back(stack, open_count, close_count + 1)
                stack.pop()

        ans = []
        back([], 0, 0)
        return ans
