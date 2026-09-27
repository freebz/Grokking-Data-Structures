# 구현

# 기본 정적 배열

class Queue:
    def __init__(self, max_size):
        if max_size <= 1:
            raise ValueError(f'큐의 크기가 잘못되었습니다. (최소 2개의 요소가 필요합니다): {max_size}')
        self._data = [None] * max_size
        self._max_size = max_size
        self._front = 0
        self._rear = 0
        self._size = 0
    

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0
    
    def is_full(self):
        return len(self) == self._max_size


# 인큐
    
    def enqueue(self, value):
        if self.is_full():
            raise ValueError('큐가 이미 가득 찼습니다!')
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._max_size
        self._size += 1


# 디큐
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError('큐가 비어 있어 요소를 꺼낼 수 없습니다.')
        value = self._data[self._front]
        self._front = (self._front + 1) % self._max_size
        self._size -= 1
        return value