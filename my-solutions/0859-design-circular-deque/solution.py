class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.deque = [0] * k  # 원형 덱을 위한 고정 크기 리스트
        self.front = 0  # 덱의 앞부분을 가리키는 인덱스
        self.rear = 0  # 덱의 뒷부분을 가리키는 인덱스
        self.size = 0  # 현재 덱의 요소 개수

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k  # 앞 부분을 순환식으로 이동
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k  # 뒷 부분을 순환식으로 이동
        self.size += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # 앞 부분을 순환식으로 이동
        self.size -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.k) % self.k  # 뒷 부분을 순환식으로 이동
        self.size -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k

