class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []
        nums = ['1','2','3','4','5','6','7','8','9','0']
        for i in logs:
            temp = i.split()
            print(temp)
            for j in temp[1:]:
                if j.isnumeric():
                    digit_log.append(i)
                    break
                else:
                    letter_log.append(i)
                    break

       

        letter_log = sorted(letter_log,key=lambda x: (x.split()[1:],x.split()[0]) )
        return letter_log + digit_log
