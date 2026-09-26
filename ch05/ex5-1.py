# 동적 배열 구현하기

# DynamicArray 클래스

class DynamicArray():
    def __init__(self, initial_capacity=1, typecode='l'):
        self._array = core.Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode


# 삽입

    def _double_size(self):
        old_array = self._array
        self._array = core.Array(self._capacity * 2, self._typecode)
        self._capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i]
    

    def insert(self, value):
        if self._size >= self._capacity:
            self._double_size()
        self._array[self._size] = value
        self._size += 1


# 검색

    def find(self, target):
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return None


# 삭제
    
    def delete(self, target):
        index = self.find(target)
        if index is None:
            raise(ValueError(f'삭제할 수 없음 {target}: 배열에 항목이 없다'))
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
        if self._capacity > 1 and self._size <= self._capacity / 4:
            self._halve_size()