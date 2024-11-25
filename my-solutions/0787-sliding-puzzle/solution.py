from collections import deque
class Solution(object):
    def slidingPuzzle(self, board):
        start = ''.join(str(cell) for row in board for cell in row)
        target = '123450'  # The target configuration
        
        # Directions for moving the blank space (0) up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Mapping of 1D indices to their valid neighbors (based on the board shape)
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        # BFS setup
        q = deque([(start, start.index('0'), 0)])  # (current_state, index_of_0, steps)
        visited = set([start])
        
        while q:
            state, zero_idx, steps = q.popleft()
            
            # Check if the target configuration is reached
            if state == target:
                return steps
            
            # Generate neighbors
            for neighbor in neighbors[zero_idx]:
                new_state = list(state)  # Convert to list for swapping
                # Swap 0 with the neighbor
                new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
                new_state = ''.join(new_state)  # Convert back to string
                
                # If the new state has not been visited, add it to the queue
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, neighbor, steps + 1))
        
        # If the target configuration is unreachable
        return -1
