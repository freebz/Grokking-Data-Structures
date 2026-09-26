# 정렬된 연결 리스트

# 중간에 삽입하기

def insert_in_sorted_list(self, new_data):
    current = self._head
    previous = None
    while current is not None:
        if current.data() >= new_data:
            if previous is None:
                self._head = Node(new_data, current)
            else:
                previous.append(Node(new_data, current))
            return
        previous = current
        current = current.next()
    if previous is None:
        self._head = Node(new_data)
    else:
        previous.append(Node(new_data, None))