array = list(input())
alphabet = [0 for i in range(26)]
for i in array:
    if ord(i) >= ord('a'):
        alphabet[ord(i) - ord('a')] += 1
    else:
        alphabet[ord(i) - ord('A')] += 1
        
max_alphabet = max(alphabet)
n_of_max = 0
for i in range(26):
    if alphabet[i] == max_alphabet:
        n_of_max += 1
        index_of_max = i
if n_of_max >= 2:
    print("?")
else:
    print(chr(index_of_max + ord('A')))
