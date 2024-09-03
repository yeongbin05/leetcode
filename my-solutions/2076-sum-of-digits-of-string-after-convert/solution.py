class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ''
        for i in s:
            convert += str(ord(i) - 96)
        print(convert,'convert')
        temp = 0
        for i in range(k):
            
            for i in str(convert) :
                temp += int(i)
            convert = temp
            temp = 0
        return convert
