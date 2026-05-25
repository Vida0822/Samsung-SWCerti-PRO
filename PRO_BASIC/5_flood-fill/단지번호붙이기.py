import sys
from collections import deque
input = sys.stdin.readline # strip()추가 안해주면 입력 데이터 맨 끝에 줄바꿈 문자를 같이 가져옴


def bfs(si, sj):
    # [0]
    global arr, v, ans, N
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    # [1]
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci+di, cj+dj

            # 범위밖
            if not (0 <= ni < N and 0 <= nj < N):
                continue

            # 미방문 & 집
            if not v[ni][nj] and arr[ni][nj] != 0:
                # 정답 처리
                cnt+=1

                # 이동 준비
                v[ni][nj] = 1
                q.append((ni, nj))

    # [2]
    ans.append(cnt)


# [0]
N = int(input())

arr = [list(map(int, input().strip())) for _ in range(N)] # map(int, "1234")가 알아서 각 글자를 숫자로 바꾼 뒤
v = [[0]*N for _ in range(N)]
ans = []

# [1]
for i in range(N):
    for j in range(N):
        if not v[i][j] and arr[i][j] != 0:
            bfs(i, j)


# [2]
print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])