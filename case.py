# s = input()
# count = 0
# for i in s:
#     if i.isupper(): count += 1

# print(s.lower()) if count <= len(s) // 2 else print(s.upper())

s=input();print([s.lower(),s.upper()][sum(map(str.isupper,s))>len(s)/2]) 

