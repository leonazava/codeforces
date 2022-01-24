n = int(input())
cnt = 0
for i in range(n):
    s = sum(map(int, input().split()))
    if s > 1: cnt += 1
print(cnt)