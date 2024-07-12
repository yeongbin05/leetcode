class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if y > x :
            a = []
            for i in s :
                a.append(i)
            stack = []
            ans = 0
            stack1 = []
            
            
            while  a :
                
                stack.append(a.pop())
               
                
                while len(stack) >= 2 and stack[-2] + stack[-1] == 'ab':
                   
                    ans += y
                    stack.pop()
                    stack.pop()
           
            stack = stack[::-1]
            while stack :
                stack1.append(stack.pop())
                while len(stack1) >= 2 and stack1[-2] + stack1[-1] == 'ba':
                   
                    ans += x
                    stack1.pop()
                    stack1.pop()
        else : 
            a = []
            for i in s :
                a.append(i)
            stack = []
            ans = 0
            stack1 = []
           
            
            while  a :
                
                stack.append(a.pop())
              
                
                while len(stack) >= 2 and stack[-2] + stack[-1] == 'ba':
                    
                    ans += x
                    stack.pop()
                    stack.pop()
           
            stack = stack[::-1]
            while stack :
                stack1.append(stack.pop())
                while len(stack1) >= 2 and stack1[-2] + stack1[-1] == 'ab':
                    
                    ans += y
                    stack1.pop()
                    stack1.pop()
        return ans                
