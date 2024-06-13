m,n,L = map(int,input().split())
xy = list(map(int,input().split()))
arr = []
count = 0
xy.sort()
for _ in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
for i in arr:
    low = (i[0] - L) + i[1]
    high = (L - i[1]) + i[0]
    l = 0
    r = len(xy) - 1
    while l <= r:
        if low <= xy[(l + r)//2] <= high:
            count += 1
            break
        if xy[(l + r)//2] < low:
            l = (l + r) // 2 + 1
        else:
            r = (l + r) // 2 -1
print(count)