class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1,n2= bin(num1)[2:],bin(num2)[2:]
        n,m = len(n1),len(n2)
        arr_n1 = [0] * (m-n) +[i for i in n1]
        arr_len = len(arr_n1)
        visited = ['0'] * arr_len
        cnt_n2 = n2.count('1')
        for i in range(len(arr_n1)):
            if cnt_n2 == 0:
                break
            if arr_n1[i] == '1':
                cnt_n2 -= 1
                arr_n1[i] = '0'
                visited[i] = '1'
        

        for i in range(arr_len-1,-1,-1):
            if cnt_n2 == 0:
                break
            if visited[i] == '0':
                cnt_n2 -= 1
                visited[i] = '1'

        ans = int(''.join(visited),2)

        return  ans
