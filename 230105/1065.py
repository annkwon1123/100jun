N = input()
hansu = 0

for i in range(1, int(N)+1):
    i = str(i)
    array = list(map(int, i))
    if len(array) <= 2:
        hansu = hansu + 1
    else:
        a0 = array[0]
        d = array[1] - array[0]
        n = 0
        for j in array:
            if j == a0 + n * d:
                n = n + 1
            else: 
                break
        if n == len(array):
            hansu = hansu + 1
        
print(hansu) 

