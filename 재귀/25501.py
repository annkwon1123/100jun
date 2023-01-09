n_of_rec = 1

def recursion(s, l, r):
    global n_of_rec 
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        n_of_rec += 1 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
for i in range(n):
    n_of_rec = 1
    str = input()
    print(isPalindrome(str), n_of_rec)
