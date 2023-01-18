N , M = map(int, input().split())
array = [list(input()) for _ in range(N)]
result = 0

if array[0][0] == "B":
    type = 0 
else:
    type = 1
        
for i in range(N):
    if i > 0 and array[i-1][0] == "B":
        type = 1
    elif i > 0 and array[i-1][0] == "W":
        type = 0
        
    for j in range(M):
        if type == 0:
            type = 1
            if array[i][j] != "B":
                result += 1
        else:
            type = 0
            if array[i][j] != "W":
                result += 1
print(result)
