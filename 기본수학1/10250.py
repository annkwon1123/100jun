N = int(input())
for i in range(N):
    H, W, O = list(map(int, input().split()))
    h = O%H
    w = int(O/H) + 1
    if h == 0: 
        h = H
        w -= 1
    print(int(str(h)+"0"+str(w)))
