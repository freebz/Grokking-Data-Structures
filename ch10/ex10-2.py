# 우선순위 큐의 실제 활용

# k개의 가장 큰 항목 찾기

def k_largest_elements(arr, k):
    heap = Heap(element_priority=lambda x: -x[1])
    for i in range(len(arr)):
        if len(heap) >= k:
            if heap.peek()[1] < arr[i]:
                heap.top()
                heap.insert((i, arr[i]))
            else:
                heap.insert((i, arr[i]))
    return [heap.top() for _ in range(k)]

print(k_largest_elements(drawn, 6))