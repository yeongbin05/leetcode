class MyCalendarTwo:

    def __init__(self):
        self.bookings1 = []  # 한 번 겹치는 예약
        self.bookings2 = []  # 두 번 겹치는 예약
        
    def book(self, start: int, end: int) -> bool:
        # 두 번 겹치는 예약과 비교
        for s, e in self.bookings2:
            if start < e and end > s:
                return False
        
        # 한 번 겹치는 예약과 비교
        for s, e in self.bookings1:
            if start < e and end > s:
                # 겹치면 두 번 겹치는 예약에 추가
                self.bookings2.append((max(start, s), min(end, e)))
        
        # 한 번 겹치는 예약에 추가
        self.bookings1.append((start, end))
        return True

