A = list(map(int, input().split()))
c = 1
for i in A:
   c = c * i ** (1/int(len(A)))

print(c)






