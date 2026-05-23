"""
도형 회전
관점1) B배열을 A에서 가져와 채우는 방식 (B배열에 대해 for 문 돌면서 A 배열에서 값 가져오기)
90º: B[i][j] = A[N-1-j][+i] --> B배열에서 col이 1 증가할 때 A 배열에서 row가 1 감소하므로  -j
180º : B[i][j] = A[-i][-j]
ㄴ tip : 증감 방향이 서로 반대면 -, 같으면 +

관점1) A배열의 값을 B로 채우는 방식 (A배열에 대해 for문 돌면서 B 배열에 채워넣기]
90º: B[j][H-1-i] = A[i][j]
"""

def rotate_90():
    global W, H, arr # 이거 헷갈리니까 담부턴 그냥 N, M (원래 쓰던거)

    # copy
    new_arr = [[0 for _ in range(H)] for _ in range(W)]

    for i in range(H):
        for j in range(W):
            new_arr[j][H-1-i] = arr[i][j]

    # 덮어쓰기
    arr = new_arr
    W, H = H, W

def up_down():
    global W, H, arr

    # copy
    new_arr = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            new_arr[i][j] = arr[H-1-i][j]

    arr = new_arr

def left_right():
    global W, H, arr

    # copy
    new_arr = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):
            new_arr[i][j] = arr[i][W-1-j]

    arr = new_arr

## main ##
# [0]
# global W, H, arr

W, H = map(int, input().split()) # 열, 행
arr = [list(input()) for _ in range(H)] # 원본 arr
C = int(input()) # 명령 코드

# [1]
if C == 0 :
    rotate_90()
elif C == 1 or C == 2:
    for _ in range(C+1):
        rotate_90() # 10^6 * 2
elif C == 3 :
    up_down()
else :
    left_right()

# [2]
print(W, H)
for i in range(H):
    print(*arr[i], sep="")
