# 배열의 실제 활용

# 통계

def max_in_array(array):
    if len(array) == 0:
        raise Exception('빈 배열에서 최댓값을 구할 수 없습니다.')
    max_index = 0
    for index in range(1, len(array)):
        if array[index] > array[max_index]:
            max_index = index
    return max_index, array[max_index]


max_in_array(counters)
> 1, 234
min_in_array(counters)
> 5, 107