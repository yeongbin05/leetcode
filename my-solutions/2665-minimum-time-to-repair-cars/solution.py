class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_time, max_time = 1, max(ranks) * (cars**2)
        while max_time >= min_time : 
            mid = (min_time+max_time) // 2
            temp = 0
            for i in ranks:
                temp += int((mid//i)**(1/2))
            if temp >= cars:
                max_time = mid - 1
            else:
                min_time = mid + 1

        return min_time
