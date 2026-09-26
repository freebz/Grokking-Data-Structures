# 이중 연결 리스트

# 2배의 링크, 2배의 재미?

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None
    
    def data(self):
        return self._data
    
    def next(self):
        return self._next
    
    def has_next(self):
        return self._next is not None
    
    def append(self, next_node):
        self._next = next_node
        if next_node is not None:
            next_node._prev = self
    
    def prev(self):
        return self._prev
    
    def has_prev(self):
        return self._prev is not None
    
    def prepend(self, prev_node):
        self._prev = prev_node
        if prev_node is not None:
            prev_node._next = self


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None


# 삽입

# 리스트의 시작에 삽입하기

    def insert_in_front(self, data):
        if self._head is None:
            self._tail = self._head = Node(data)
        else:
            old_head = self._head
            self._head = Node(data)
            self._head.append(old_head)


# 리스트트 끝에 삽입하기
    
    def insert_to_back(self, data):
        if self._tail is None:
            self._tail = self._head = Node(data)
        else:
            old_tail = self._tail
            self._tail = Node(data)
            self._tail.prepend(old_tail)


# 삭제

    def delete(self, target):
        node = self._search(target)
        if node is None:
            raise ValueError(f'{target} 값을 가진 요소를 목록에서 찾을 수 없습니다.')
        if node.prev() is None:
            self._head = node.next()
            if self._head is None:
                self._tail = None
            else:
                self._head.prepend(None)
        elif node.next() is None:
            self._tail = node.prev()
            self._tail.append(None)
        else:
            node.prev().append(node.next())
            del node