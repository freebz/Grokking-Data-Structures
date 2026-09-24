# 배열에 대한 작업

# 정렬되지 않은 배열을 위한 클래스

class UnsortedArray :
    def __init__(self, max_size, typecode = 'l'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0


# 새로운 항목 추가

    def insert(self, new_entry):
        if self._size >= len(self._array):
            raise ValueError('배열이 이미 가득 찼습니다')
        else:
            self._array[self._size] = new_entry
            self._size += 1


# 항목 제거
    
    def delete(self, index):
        if self._size == 0:
            raise ValueError('빈배열은 삭제할 수 없습니다.')
        elif index < 0 or index >= self._size:
            raise ValueError(f'인덱스 {index}가 범위를 벗어났습니다.')
        else:
            self._array[index] = self._array[self._size-1]
            self._size -= 1


# 값의 검색
    
    def find(self, target):
        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        return None


# 순회
    
    def traverse(self, callback):
        for index in range(self._size):
            callback(self._array[index])


array.traverse(print)