class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0

        total_teams = 0
        
        # Iterate over each soldier as the middle soldier in the team
        for j in range(n):
            less_left = 0
            greater_left = 0
            less_right = 0
            greater_right = 0
            
            # Count number of soldiers with less and greater rating to the left of j
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                elif rating[i] > rating[j]:
                    greater_left += 1
            
            # Count number of soldiers with less and greater rating to the right of j
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    less_right += 1
                elif rating[k] > rating[j]:
                    greater_right += 1
            
            # Calculate number of valid teams with rating[j] as the middle soldier
            total_teams += less_left * greater_right
            total_teams += greater_left * less_right
        
        return total_teams
