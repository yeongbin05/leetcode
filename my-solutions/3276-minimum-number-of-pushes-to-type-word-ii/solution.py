class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = {}
        for i in word:
            if i in dic:
                dic[i] += 1
            else :
                dic[i] = 1
        sorted_dic = dict(sorted(dic.items(), key=lambda x: -x[1]))
        print(sorted_dic)
        temp = 1
        cnt = 0
        ans = 0
        for j in sorted_dic :
            if cnt == 8 :
                temp += 1
                cnt = 0
            ans += (temp * sorted_dic[j])
            cnt += 1
        return ans
