n,m = map(int,input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
l = 1
r = m * max(arr)
mi = 99999999999999999999999999999
while l <= r:
    count = 0
    for i in arr:
        num = ((l + r) // 2) // i
        count += num
    if count >= m and mi > (l + r) // 2:
        mi = (l + r) // 2
        r = (l + r) // 2 -1
    else:
        l = (l + r) // 2 + 1
print(mi)