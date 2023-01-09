array = list(input())
alphabet = [-1 for i in range(26)]
for i in range(len(array)):
    letter = array[i]
    index = ord(letter) - ord('a')
    if alphabet[index] == -1:
        alphabet[index] = i
print(*alphabet)
