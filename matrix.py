for i in range(5):
    line = list(map(int, input().split()))
    for j in range(5):
        if line[j] == 1:
            print(abs(i - 2) + abs(j - 2))
         
   

