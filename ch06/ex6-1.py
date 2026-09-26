# 단일 연결 리스트

# 단일 연결 리스트 구현

class Node:
    def __init__(self, data, next_node = None):
        self._data = data
        self._next = next_node
    
    def data(self):
        return self._data
    
    def next(self):
        return self._next
    
    def has_next(self):
        return self._next is not None
    
    def append(self, next_node):
        self._next = next_node


class SinglyLinkedList:
    def __init__(self):
        self._head = None


# 삽입
    
    def insert_to_back(self, data):
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))
    

    def insert_in_front(self, data):
        old_head = self._head
        self._head = Node(data, old_head)


# 검색
    
    def _search(self, target):
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None


# 삭제
    
    def delete(self, target):
        current = self._head
        previous = None
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError(f'{target} 값을 가진 요소를 목록에서 찾을 수 없습니다.')