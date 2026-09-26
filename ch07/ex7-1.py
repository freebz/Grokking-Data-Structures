# 가장 기본적인 컨테이너: 가방

# Bag 클래스

class Bag:
    def __init__(self):
        self._data = SinglyLinkedList()


# 삽입
    
    def insert(self, value):
        self._data.insert_in_front(value)


# 순회
    
    def traverse(self):
        return self._data.traverse()