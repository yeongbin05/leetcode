class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = [i.split() for i in logs]
        letter_logs = []
        digit_logs  =[]
        for i in logs:
            if i[1][0] in '0123456789' :
                digit_logs.append(i)
            else:
                letter_logs.append(i)
        

        letter_logs.sort(key = lambda x : (x[1:],x[0]))
        letter_logs = [' '.join(i) for i in letter_logs]
        digit_logs = [' '.join(i) for i in digit_logs]
        return letter_logs + digit_logs
