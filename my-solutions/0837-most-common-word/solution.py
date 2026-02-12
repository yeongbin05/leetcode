class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_paragraph = []
        for ch in paragraph:
            if ch == ' ' or ch.isalpha():
                new_paragraph.append(ch.lower())
            else:
                new_paragraph.append(' ')
        
        paragraph = ''.join(new_paragraph).split()
        ban_set = set()
        for i in banned:
            ban_set.add(i)
        dic = {}
        # print(paragraph,ban_set)
        ans_cnt,ans_word = 0,''
        for ch in paragraph:
            if ch not in ban_set :
                if ch not in dic:
                    dic[ch] = 1
                else:
                    dic[ch] += 1

                if dic[ch] > ans_cnt:
                    ans_cnt = dic[ch]
                    ans_word = ch
        # print(dic)
        return ans_word
