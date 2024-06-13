a = int(input())
m = 0
memo = set()
arr = list(map(int,input().split()))
for i in arr:
    m += i
def f(p,i):
    global memo
    if p > 0 and p <= m:
        memo.add(p)
    if i >= len(arr):
        return
    f(p + arr[i],i + 1)
    f(p,i + 1)
    f(p - arr[i],i + 1)
f(0,0)
print(m - len(memo))