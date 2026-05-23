# [0]
Q = int(input())
db = set()

# [1]
for _ in range(Q):
    lst = tuple(map(int, input().split()))

    # 방법 1
    # key 값을 tuple 형태로 사용하기
    # if lst in db:
    #     db.remove(lst)
    # else:
    #     db.add(lst)


    # 방법 2
    # key 값을 하나의 10진수(int)로 변경하여 사용하기
    base = [1, 1004, 1004**2, 1004**3, 1004**4] # 가능한 정수 범위 : 1~1004
    #  :이 때, 서로 다른 배열 구성이 같은 key 값이 나오지 않도록 진법을 정의해주는 것이 좋음
    #   ex. 0~1004가 가능한 정수, (1004, 0) != (0, 1) -> 둘다 key값이 1004 가 나옴 --> 1005 로  설정해야함

    key = sum([lst[i]*base[i] for i in range(5)])
    if key in db:
        db.remove(key)
    else:
        db.add(key)

# [2]
print(len(db))