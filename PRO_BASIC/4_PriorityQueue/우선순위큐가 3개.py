import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

# [0]
max_hq, min_pq, abs_pq = [], [], []
q = int(input()) # 10^5

# [1] & [2] : 실행 중 정답 출력
for _ in range(q):
    x = int(input())

    if x != 0:
        heappush(max_hq, -x)
        heappush(min_pq, x)
        heappush(abs_pq, (abs(x), x)) # 1순위 : 절대값이 작은 순, 2순위 : 값이 작은 순
    else:
        if not max_hq:
            print(-1)
        else:
            print(-heappop(max_hq), heappop(min_pq), heappop(abs_pq)[1], sep=" ")
