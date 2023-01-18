array = list(map(int, input().split()))
print(array)
print(array.sort())
print(array.sort(reverse=True))

if array == array.sort():
    print("ascending")
elif array == array.sort(reverse=True):
    print("descending")
else:
    print("mixed")
