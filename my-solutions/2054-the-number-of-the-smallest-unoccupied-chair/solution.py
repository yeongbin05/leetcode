import heapq
class Solution(object):
    def smallestChair(self, times, targetFriend):

        n = len(times)
    
        # 친구들의 도착 시간 기준으로 정렬된 리스트를 만듭니다.
        arrivals = sorted((time[0], time[1], i) for i, time in enumerate(times))
        
        # 사용 가능한 의자 번호를 관리할 최소 힙.
        free_chairs = list(range(n))  # 최소 n개의 의자 필요.
        heapq.heapify(free_chairs)
        
        # 친구들이 떠날 때 사용 중인 의자들을 관리할 최소 힙.
        # (떠나는 시간, 의자 번호) 형태로 저장합니다.
        occupied_chairs = []
        
        # 친구들의 의자 배정을 기록할 리스트.
        friend_to_chair = [0] * n
        
        # 도착 시간 순서대로 친구들을 처리합니다.
        for arrive, leave, friend in arrivals:
            # 친구가 도착하기 전에 먼저 떠나는 친구들의 의자를 반환합니다.
            while occupied_chairs and occupied_chairs[0][0] <= arrive:
                _, chair = heapq.heappop(occupied_chairs)
                heapq.heappush(free_chairs, chair)
            
            # 현재 사용 가능한 가장 작은 번호의 의자를 할당합니다.
            chair = heapq.heappop(free_chairs)
            friend_to_chair[friend] = chair
            
            # 현재 친구가 사용할 의자를 occupied_chairs에 추가합니다.
            heapq.heappush(occupied_chairs, (leave, chair))
            
            # targetFriend라면 해당 의자 번호를 반환합니다.
            if friend == targetFriend:
                return chair
