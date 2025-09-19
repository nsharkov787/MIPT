d = open('input.txt').read().split()
print(d)
operation = d[-1]
r = 0
b = []
for i in range(len(d)-1): b.append(float(d[i]))
print(b)
if operation == '+': r = sum(b)

if operation == ('-'): r = b[0] - sum(b[1:])
if operation == ('*'):
    r = 1
    for i in b:
        r = r*i
f= open('output.txt', 'w')
f.write(str(r))
f.close()









