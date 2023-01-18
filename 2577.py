A = int(input())
B = int(input())
C = int(input())
array = list(map(int, str(A*B*C)))
result = [0 for i in range(9)]
print(array)
for i in array:
    result[i] += 1
print(result)
for i in result:
    print(i)
