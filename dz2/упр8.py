a = input()
b = list(map(int, input().split()))
for i in b:
    count = 0
    for x in b:
        if x < i:
            count += 1
    if count == len(b) // 2:
        print(str(i))