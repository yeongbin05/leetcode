class Solution:
    def maximum69Number (self, num: int) -> int:
        n = len(str(num))
        st_num = list(str(num))
        for i in range(n):
            if st_num[i] == '6':
                st_num[i] = '9'
                break

        # print(st_num)
        return int(''.join(st_num))
