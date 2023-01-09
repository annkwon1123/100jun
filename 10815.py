sang_N = int(input())
sang_cards = list(map(int, input().split()))
sang_cards = sang_cards.sort()
N = int(input())
cards = list(map(int, input().split()))

result = [0 for i in range(N)]
j = 0
for i in range(N):
    if type(sang_cards[i]) == int and cards[i] == sang_cards[j]:
        result[i] = 1
    j += 1

print(*result)
