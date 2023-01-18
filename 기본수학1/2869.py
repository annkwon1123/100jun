A, B, V = map(int, input().split())
V -= A
day = 1 + int(V/(A-B))
if V/(A-B) > int(V/(A-B)):
  day += 1
print(day)
