a = list(map(int, input().split()))
b = 0
c = 0
for i in a:
    if a.count(i) > b:
        b = a.count(i)
        c = i
print(c)