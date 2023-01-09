N = int(input())
result = 0
for i in range(N-2,int(N/2),-1):
    D = i
    D_array = list(map(int, str(i)))
    for j in D_array:
        D += j
        
    if D == N:
        result = i
        
print(result)
