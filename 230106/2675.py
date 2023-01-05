array = list(input())
n = int(array[0])
result = ""
for i in range(2, len(array)):
    for j in range(n):
        result = result + array[i]
        
print(result)

