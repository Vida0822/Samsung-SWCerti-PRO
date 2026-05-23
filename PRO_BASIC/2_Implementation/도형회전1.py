def rotate_90():
    global W, H, arr

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





