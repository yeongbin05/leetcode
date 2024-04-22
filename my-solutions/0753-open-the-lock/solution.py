from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        queue = deque([('0000', 0)])
    
        # Set to store the deadends for quick lookup
        dead_set = set(deadends)
        
        # Set to store visited states
        visited = set()
        
        # BFS
        while queue:
            # Pop the current state and its number of turns
            current, turns = queue.popleft()
            
            # Check if we reached the target
            if current == target:
                return turns
            
            # Check if the current state is a deadend or visited
            if current in dead_set or current in visited:
                continue
            
            # Mark the current state as visited
            visited.add(current)
            
            # Generate next states by changing one digit at a time
            for i in range(4):
                digit = int(current[i])
                
                # Move up (increment)
                next_up = current[:i] + str((digit + 1) % 10) + current[i+1:]
                # Move down (decrement)
                next_down = current[:i] + str((digit - 1) % 10) + current[i+1:]
                
                # Add the next states to the queue
                queue.append((next_up, turns + 1))
                queue.append((next_down, turns + 1))
        
        # If target is unreachable
        return -1
