
n, h = map(int, input().split())
a = list(map(int, input().split()))

width = n

for i in range(n):
    if a[i] > h:
        width += 1

print(width)

