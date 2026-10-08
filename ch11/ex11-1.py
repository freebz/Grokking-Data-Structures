# 이진 탐색 트리

# 클래스 정의와 생성자

class Node:
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right
    def set_left(self, node):
        self._left = node
    def set_right(self, node):
        self._right = node


# 최솟값과 최댓값 찾기
    
    def find_max_in_subtree(self):
        parent = None
        node = self
        while node.right() is not None:
            parent = node
            node = node.right()
        return node, parent


class BinarySearchTree:
    def __init__(self):
        self._root = None


# 탐색
    
    def _search(self, value):
        parent = None
        node = self._root
        while node is not None:
            node_val = node.value()
            if node_val == value:
                return node, parent
            elif value < node_val:
                parent = node
                node = node.left()
            else:
                parent = node
                node = node.right()
        return None, None


# 삽입
    
    def insert(self, value):
        node = self._root
        if node is None:
            self._root = BinarySearchTree.Node(value)
        else:
            while node is not None:
                if value <= node.value():
                    if node.left() is None:
                        node.set_left(BinarySearchTree.Node(value))
                        break
                    else:
                        node = node.left()
                elif node.right() is None:
                    node.set_right(BinarySearchTree.Node(value))
                    break
                else:
                    node = node.right()


# 삭제
    
    def delete(self, value):
        if self._root is None:
            raise ValueError('빈 트리에서 삭제할 수 없습니다.')
        node, parent = self._search(value)
        if node is None:
            raise ValueError('값을 찾을 수 없습니다.')
        if node.left() is None or node.right() is None:
            maybe_child = node.right() if node.left() is None else node.left()
            if parent is None:
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        else:
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None:
                new_node = BinarySearchTree.Node(max_node.value(), None, node.right())
            else:
                new_node = BinarySearchTree.Node(
                    max_node.value(),
                    node.left(),
                    node.right())
                max_node_parent.set_right(max_node.left())
            if parent is None:
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)