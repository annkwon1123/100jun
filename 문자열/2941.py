letters = list(input())
length = len(letters)
n_of_letters = 0
i = 0
while i < length:
    if i+1 < length and letters[i] == 'c' and (letters[i+1] == '=' or letters[i+1] == '-'):
        i += 1
    elif i+1 < length and letters[i+1] == 'j' and (letters[i] == 'l' or letters[i] == 's'):
        i += 1
    elif i+1 < length and letters[i+1] == '=' and (letters[i] == 's' or letters[i] == 'z'):
        i += 1
    elif i+1 < length and letters[i] == 'd' and letters[i+1] == '-':
        i += 1
    elif i+2 < length and letters[i] == 'd' and letters[i+1] == 'z' and letters[i+2] == '=':
        i += 2
    print(n_of_letters, i)
    n_of_letters += 1    
    i += 1
    
print(n_of_letters)
