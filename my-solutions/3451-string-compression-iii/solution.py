class Solution(object):
    def compressedString(self, word):
        # temp = word[0]
        # ans = ""
        # cnt = 0
        # for i in word:
        #     if cnt < 9 and i == temp[-1]:
        #         temp += i
        #         cnt += 1
        #     elif i != temp[-1] or cnt >= 9:
        #         ans += str(cnt)
        #         ans += temp[-1]
        #         cnt = 1
        #         temp = i
                         
        # ans += str(cnt)
        # ans += temp[-1]
        

        # return ans
        ans = []
        cnt = 1
        temp = word[0]

        for i in range(1, len(word)):
            if word[i] == temp and cnt < 9:
                cnt += 1
            else:
                ans.append("{}{}".format(cnt, temp))  # 그룹을 결과 리스트에 추가
                cnt = 1
                temp = word[i]

        # 마지막 남은 문자 그룹 추가
        ans.append("{}{}".format(cnt, temp))

        return ''.join(ans)  
