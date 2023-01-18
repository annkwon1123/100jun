T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    if K == 0:
        people = N
    else:
        people = 1
        for i in range(N-1, N+K):
            people *= i+1
        for i in range(K+1):
            people /= i+1
    print(int(people))
