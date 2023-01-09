N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_of_total = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if M - total >= 0 and total > max_of_total:
                max_of_total = total
print(max_of_total)
