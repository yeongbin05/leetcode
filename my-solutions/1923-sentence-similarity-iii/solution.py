class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        sentence1 = list(sentence1.split())
        sentence2 = list(sentence2.split())
        len_sentence1 = len(sentence1)
        len_sentence2 = len(sentence2)
        ans = False
        
        if len_sentence1 > len_sentence2 :
            for i in range(len_sentence2) :
                if sentence1[i] == sentence2[i] :
                    continue
                
                for j in range(len_sentence2-i):
                    if sentence1[-j-1] == sentence2[-j-1]:
                        continue
                    else:
                        return ans
                ans = True
                return ans

            ans = True
            return ans
        
        elif len_sentence1 < len_sentence2 :
            for i in range(len_sentence1) :
                if sentence1[i] == sentence2[i] :
                    continue
                
                for j in range(len_sentence1-i):
                    if sentence1[-j-1] == sentence2[-j-1]:
                        continue
                    else:
                        return ans
                ans = True
                return ans

            ans = True
            return ans

        else :
            if sentence1 == sentence2 :
                return True

            return False
