class Solution:
    def isPalindrome(self, s: str) -> bool:
        # test = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d',
        # 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
        # 'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        # 'O','P','Q','R','S','T','U','V','W','X','Y','Z']
        # s = list(_.lower() for _ in s if _ in test)
        # if s == s[::-1] :
        #     return True

        # return False

        # s = s.lower()
        # s= re.sub('[^a-z0-9]','',s)
        # return s==s[::-1]
        strippedString = ''.join(filter(lambda char : char.isalnum(), s.lower()))
        return strippedString == strippedString[::-1]
