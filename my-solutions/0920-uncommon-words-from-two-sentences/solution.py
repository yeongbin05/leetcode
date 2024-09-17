class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        # arr1 = [_ for _ in s1.split()]
        # arr2 = [_ for _ in s2.split()]
        # dic1 = {}
        # dic2 = {}
        # ans = []
        # for i in arr1 :
        #     if i in dic1:
        #         dic1[i] += 1
        #     else :
        #         dic1[i] = 1
        # for i in arr2 :
        #     if i in dic2:
        #         dic2[i] += 1
        #     else :
        #         dic2[i] = 1

        # for i in dic1:
        #     if dic1[i] == 1 and i not in dic2 :
        #         ans.append(i)
        # for i in dic2:
        #     if dic2[i] == 1 and i not in dic1:
        #         ans.append(i)
        # return ans
        combined = s1.split() + s2.split()
        count = Counter(combined)

        # 등장 횟수가 1인 단어만 리스트에 추가
        return [word for word, freq in count.items() if freq == 1]
