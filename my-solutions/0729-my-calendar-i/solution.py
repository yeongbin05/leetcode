class MyCalendar(object):
    
    def __init__(self):
        self.bookings = []
    def book(self, start, end):
        for s, e in self.bookings:  # 이미 예약된 구간과 비교
            if start < e and end > s:  # 구간이 겹치면
                return False
        self.bookings.append((start, end))  # 겹치지 않으면 예약 추가
        return True
