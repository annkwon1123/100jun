result = [0 for i in range(10000+1)]

for i in range(1, 10000+1):
    d = i
    array = list(map(int, str(i))) 
    
    for j in range(len(array)):
        d = d + array[j]
    if d <= 10000:
        result[d] = 1
    
for i in range(1, 10000+1):
    if result[i] == 0:
        print(i)
    
