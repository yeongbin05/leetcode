class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_idx = {}
        for idx,val in enumerate(s):
            last_idx[val] = idx
        for idx,val in enumerate(s):
            if val in stack:
                continue
            while stack and val < stack[-1] and last_idx[stack[-1]] > idx:
                stack.pop()
            stack.append(val)


        return ''.join(stack)
