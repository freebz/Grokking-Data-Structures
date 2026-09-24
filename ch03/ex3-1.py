# 정렬된 배열 구현

class SortedArray():
    def __init__(self, max_size, typecode = 'l'):
        self._array = core.Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0


# 삽입
    
    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError(f'배열이 이미 가득 찼습니다. 최대 크기: {self._max_size}')
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i-1]
        self._array[0] = value
        self._size += 1


# 삭제
    
    def delete(self, target):
        index = self.search(target)
        if index is None:
            raise ValueError(f'요소 {target}을(를) 삭제할 수 없습니다: 해당 항목이 배열에 없습니다.')
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1


# 선형 탐색
    
    def linear_search(self, target):
        for i in range(self._size):
            if self._array[i] == target:
                return i
            elif self._array[i] > target:
                return None
        return None


# 이진 탐색
    
    def binary_search(self, target):
        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return None