class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        import math
    
        n = len(source)
        
        # Initialize the conversion cost table
        inf = float('inf')
        conversion_cost = {char: {char2: inf for char2 in set(original + changed)} for char in set(original + changed)}
        
        # Fill the conversion cost with direct conversion rules
        for o, c, co in zip(original, changed, cost):
            conversion_cost[o][c] = min(conversion_cost[o][c], co)
        
        # Use Floyd-Warshall to compute the minimum conversion cost between all characters
        characters = list(conversion_cost.keys())
        for k in characters:
            for i in characters:
                for j in characters:
                    if conversion_cost[i][j] > conversion_cost[i][k] + conversion_cost[k][j]:
                        conversion_cost[i][j] = conversion_cost[i][k] + conversion_cost[k][j]

        total_cost = 0
        
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            min_cost = inf
            # If we can change s_char to t_char directly or indirectly
            if s_char in conversion_cost and t_char in conversion_cost[s_char]:
                min_cost = conversion_cost[s_char][t_char]
            
            if min_cost == inf:
                return -1  # It's impossible to convert source to target
            
            total_cost += min_cost
        
        return total_cost
            
