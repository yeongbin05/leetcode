class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []
        
        for position, health, direction, index in robots:
            if direction == 'R':
                stack.append((position, health, direction, index))
            else:
                while stack and stack[-1][2] == 'R':
                    r_position, r_health, r_direction, r_index = stack.pop()
                    if r_health > health:
                        health = 0
                        stack.append((r_position, r_health - 1, r_direction, r_index))
                        break
                    elif r_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                if health > 0:
                    stack.append((position, health, direction, index))
        
        surviving_robots = sorted(stack, key=lambda x: x[3])
        return [health for _, health, _, _ in surviving_robots]
