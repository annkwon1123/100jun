N = int(input())
level = 1
while N > 1 and N > level:
    N = N - level
    level += 1
    
print(level-N+1, "/", N, sep="")
