n = int(input())
need = -1

a = int(n/3)
b = int(n/5)
for j in range(b+1):
    for i in range(a+1):
        if 3*i + 5*j == n:
            need = i + j
print(need)
