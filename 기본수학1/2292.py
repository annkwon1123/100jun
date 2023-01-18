#1 1개: 1레벨
#2~7 6개: 2레벨
#8~19 12개: 3레벨
#20~37 18개: 4레벨
#38~61 24개: 5레벨

N = int(input())
level = 1
i = 1
while N > 1:
    N = N - 6*i
    level += 1
    i += 1
print(level)
