# 충돌 해결

# 체이닝

class HashTable:
    __A__ = Decimal((sqrt(5) - 1) / 2)
    def __init__(self, buckets, extract_key=hash):
        self._m = buckets
        self._data = [SinglyLinkedList() for _ in range(buckets)]
        self._extract_key = extract_key
    def _hash(self, key):
        return floor(self._m * ((Decimal(key) * HashTable.__A__) % 1))
    

    def insert(self, value):
        index = self._hash(self._extract_key(value))
        self._data[index].insert_in_front(value)
    

    def _search(self, value):
        index = self._hash(key)
        value_matches_key = lambda v: self._extract_key(v) == key
        return self._data[index].search(value_matches_key)
    

    def delete(self, value):
        index = self._hash(self._extract_key(value))
        self._data[index].delete(value)