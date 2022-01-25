# import math
# a = list(map(int, input().split(" ")))

# gcd = math.gcd((7 -max(a)), 6)
# x = int((7 - max(a)) / gcd) 
# y = int(6 / gcd)
# print("{}{}{}".format(x, "/", y))

print(['1/1','5/6','2/3','1/2','1/3','1/6'][max(map(int,input().split()))-1])
