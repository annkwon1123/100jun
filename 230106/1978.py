N = int(input())
array = list(map(int, input().split()))
count = 0
for i in range(len(array)):
    if array[i] < 2:
        check = False
    else:
        check = True
        
    for j in range(2, array[i]):
        if array[i]%j == 0:
            check = False
    if check == True:
        count += 1
print(count)
