# wq = int(input()) 
# wires=[]
# count = 0
# for i in list(map(int, input().split(" "))):
#     wires.append(i)
# shots = int(input()) 
# for i in range(shots):
#     foo = list(map(int, input().split(" ")))
#     prev = foo[0] - 2
#     curr = foo[0] - 1
#     next = foo[0] 
#     bird = foo[1]
#     if curr<=shots-2 or wires[next]:
#         wires[next] = wires[next] + (wires[curr] - bird)
#     if prev >= 0:
#         wires[prev] = wires[prev] + (wires[curr] - (wires[curr] - bird) - 1)
#     wires[curr] = 0
# for i in range(wq):
#     print(wires[i])

i=lambda:[*map(int,input().split())]
n=i()[0];a=[0]+i()+[0]
for _ in[0]*i()[0]:x,y=i();a[x-1]+=y-1;a[x+1]+=a[x]-y;a[x]=0
print(*a[1:n+1],sep='\n')

