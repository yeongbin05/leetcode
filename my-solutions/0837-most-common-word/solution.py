class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [_ for _ in paragraph]
        for i in range(len(paragraph)):
            if not paragraph[i].isalnum():
                paragraph[i] = ''
        
        paragraphs = ''
        temp =  ''
        flag = True
        for i in paragraph:
            flag = True
            if i != '' :
                temp += i
            else :
                paragraphs += temp
                paragraphs += ' ' 
                
                temp = ''
                flag = False
        if flag == True:
            paragraphs += temp
        dic = {}
        print(paragraphs,'paragraphs1')
        paragraphs = paragraphs.split()
        print(paragraph,'paragraph')
        print(paragraphs,'paragraphs')
        for i in paragraphs:
            i = i.lower()
            if i not in banned:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
        cnt = 0
        ans = ''
        print(dic)
        for i in dic :
            if dic[i] > cnt :
                ans = i
                cnt = dic[i]

        return ans

