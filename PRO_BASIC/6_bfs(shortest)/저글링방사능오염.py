"""
답은 똑같이 나오는데 채점할 때만 runtime error -> 시간 초과
=> 최단 거리 로직으로 변경

"""
from collections import deque

def bfs(si, sj):
    # 0)
    q = deque()
    global v

    # 1)
    q.append((3, si, sj))  # dist, si, sj
    v[si][sj] = 3

    # 2)
    while q:
        dist, ci, cj = q.popleft()

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj

            if not (0 <= ni < N and 0 <= nj < M): # 범위밖
                continue
            if arr[ni][nj] == 0:  # 그냥 길
                continue
            if v[ni][nj] != -1 and v[ni][nj] < dist+1: # 최단 거리 X
                continue

            q.append((dist + 1, ni, nj))
            v[ni][nj] = dist + 1


# [0]
M, N = map(int, input().split()) # N <= 10^2
arr = [list(map(int, list(input().strip()))) for _ in range(N)] # 1: 저글링
sj, si = map(int, input().split())
si, sj = si-1, sj-1

# [1]
v = [[-1]*M for _ in range(N)] # 방문 배열이자 최단거리 기록 배열
if arr[si][sj] == 1 :
    bfs(si, sj)

# [2]
ans1 = max([max(v[i]) for i in range(N)])
ans2 = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and v[i][j] == -1 :
            ans2+=1

print(ans1, ans2, sep="\n")


"""
[해설 풀이] 
* BFS에서 특정 노드에 처음 도달한 순간이 무조건 최단거리이다
* 가장 마지막에 방문한 노드 == 가장 먼 노드
* 원본 배열을 변경하는 방식으로 simple하게  
"""

M, N = map(int,input().split())
A = [[]]+[['']+list(input().strip()) for _ in range(N)]

# A = [[]]
# for _ in range(N):
#     A.append([''] + list(input().strip()))

sc, sr = map(int,input().split())

def bfs(sr, sc):
    que = deque([(sr,sc,3)])
    A[sr][sc] = '0'

    while que:
        r, c, sec = que.popleft()
        for dr, dc in zip([-1,0,1,0],[0,1,0,-1]):
            nr, nc = r+dr, c+dc
            if nr<1 or nr>N or nc<1 or nc>M: continue
            if A[nr][nc] == '0': continue
            que.append((nr,nc,sec+1))
            A[nr][nc] = '0'

    print(sec)

    print(sum(a.count('1') for a in A))

    cnt = 0
    for a in A: cnt += a.count('1')
    print(cnt)

bfs(sr,sc)




