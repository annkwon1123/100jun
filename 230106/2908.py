a, b = input().split()
a_array = list(a)
b_array = list(b)

len_a = len(a_array)
len_b = len(b_array)

a2 = 0
b2 = 0

for i in range(len_a):
    a2 += int(a_array[i]) * 10**i
for i in range(len_b):
    b2 += int(b_array[i]) * 10**i
    
if a2 > b2:
    print(a2)
else:
    print(b2)
