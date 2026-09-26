# 점근적 분석의 예

# 선형 탐색

def linear_search(self, target):
    for i in range(self._size):         # F(n)번 반복
        if self._array[i] == target:    # 비용: O(1)
            return i                    # 비용: O(1)
        elif self._array[i] > target:   # 비용: O(1)
            return None                 # 비용: O(1)
    return None                         # 비용: O(1)


# 이진 탐색

def binary_search(self, target):
    left = 0                                # O(1)
    right = self._size - 1                  # O(1)
    while left <= right:                    # O(1), G(n)번 반복
        mid_index = (left + right) // 2     # O(1)
        mid_val = self._array[mid_index]    # O(1)
        if mid_val == target:               # O(1)
            return mid_index                # O(1)
        elif mid_val == target:             # O(1)
            right = mid_index - 1           # O(1)
        else:
            left = mid_index + 1            # O(1)
    return None                             # O(1)