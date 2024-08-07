class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Words for the numbers
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                    "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        # Helper function to convert numbers less than 1000
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)
        
        result = ""
        for i, chunk in enumerate(self.splitByThousand(num)):
            if chunk != 0:
                result = helper(chunk) + thousands[i] + " " + result
        
        return result.strip()
    
    def splitByThousand(self, num):
        chunks = []
        while num > 0:
            chunks.append(num % 1000)
            num //= 1000
        return chunks

