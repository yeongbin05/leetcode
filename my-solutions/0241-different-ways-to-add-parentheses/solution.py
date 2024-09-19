class Solution(object):
    def diffWaysToCompute(self, expression):
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        # Iterate over the expression and divide it at each operator
        for i, char in enumerate(expression):
            if char in "+-*":
                # Recursively solve for the left and right parts
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results from the left and right sides based on the operator
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)
        
        return results

