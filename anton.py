q = int(input())
g = input()

anton = 0
danik = 0

for i in g:
    if i == "D":
        danik += 1
    else:
        anton += 1

if anton > danik:
    print("Anton")
elif anton == danik:
    print("Friendship")
else:
    print("Danik")

 


