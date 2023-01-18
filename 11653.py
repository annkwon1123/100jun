def least_prime(N):
    for i in range(2, N):
        for j in range(2, i):
            if i % j != 0:
                return i
    return N
        
N = int(input())

while N > 1:
    print(least_prime)
    if N % least_prime(N) == 0:
        print(least_prime(N))
    N = int(N / least_prime(N))    
        
