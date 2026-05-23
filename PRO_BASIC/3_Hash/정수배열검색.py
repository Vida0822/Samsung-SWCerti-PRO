# [0]
Q = int(input())
db = set()

# [1]
for _ in range(Q):
    lst = tuple(map(int, input().split()))

    if lst in db:
        db.remove(lst)
    else:
        db.add(lst)


# [2]
print(len(db))