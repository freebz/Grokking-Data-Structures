# 연결 리스트 구현

class Stack:
    def __init__(self):
        self._data = SinglyLinkedList()


# push
    
    def push(self, value):
        self._data.insert_in_front(value)


# pop
    
    def pop(self):
        if self.is_empty():
            raise ValueError("빈 스택에서 pop할 수 없습니다.")
        return self._data.delete_from_front()


# peek
    
    import copy
    def peek(self):
        if self.is_empty():
            raise ValueError("빈 스택에서 peek할 수 없습니다.")
        return copy.deepcopy(self._data._head.data())