# 딕셔너리 문제

# 중복 제거

tmp = []
for c in C:
    if not c in D:
        D.add(c)
        tmp.append(c)
C = tmp


counters = {}
for c in C:
    counters[c] = counters.get(c, 0) + 1