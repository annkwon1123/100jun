N = int(input())
count = 0

for i in range(N):
    alphabet = [0 for i in range(27)]
    letters = list(input())
    pre_index = ord(letters[0]) - ord('a')
    
    for j in letters:
        index = ord(j) - ord('a')
        if index != pre_index: # 문자가 한 세트 나옴
            alphabet[pre_index] = 1 
        if alphabet[index] == 1: 
            alphabet[index] = 2
            break
        pre_index = index
        
    if max(alphabet) != 2:
        count += 1
        
print(count)
