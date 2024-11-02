class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if sentence[0] != sentence[-1]:
            return False
        sentence = list(sentence.split())
        for i in range(len(sentence)-1):
            if sentence[i][-1] != sentence[i+1][0]: 
                return False

        
        return True
