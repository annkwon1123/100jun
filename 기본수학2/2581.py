N = int(input())
M = int(input())

prime = []
for i in range(N, M+1):
    prime_check = True
    for j in range(2, i):
        if i % j == 0: # not prime
            prime_check = False
            break
    if prime_check == True: 
        prime.append(i)
        
print(prime)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
