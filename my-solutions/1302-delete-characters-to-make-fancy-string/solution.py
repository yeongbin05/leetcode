class Solution(object):
    def makeFancyString(self, s):
        temp = ''
        ans = ''
        for i in s:
            if not temp :
                temp += i
            elif len(temp) == 1 :

                if i == temp[-1] :
                    temp += i
                    continue

                else :
                    ans += temp
                    temp = i

            elif len(temp) == 2 :
                if i == temp[-1]:
                    continue

                else :
                    ans += temp
                    temp = i
            
        ans += temp
        return ans
