t = int(input())
for i in range(t):
    array = list(input())
    n = int(array[0])
    if len(array) >= 3:
        result = ""
        for j in range(2, len(array)):
            for k in range(n):
                result = result + array[j]
        print(result)
