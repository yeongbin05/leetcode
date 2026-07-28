class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        s = sorted(s)
        ans = [0] * n
        # s순회하는 인덱스 , ans삽입을 위한 left,right
        start,left,right = 0, 0 ,  n-1
        
        while 1:
            print(start)
            if start == n-1:
                ans[n//2] = s[start]
                start += 1
                break
            if s[start] == s[start+1]:
                ans[left] = s[start]
                ans[right] = s[start+1]
                start += 2
                left += 1
                right -= 1
            
            else:
                ans[n//2] = s[start]
                start += 1

            if start >= n :
                break

        
        return ''.join(ans)
            
