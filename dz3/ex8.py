f = open('LICENSE.txt').read().lower().split()
d = {}
for i in f:
    if i in d.keys():d[i]+=1
    else:d[i]=1
print(d)
b=[]
for k in d.keys():b.append(d[k])
a = set(b)
i=0
while i < 10:
    for k in d.keys():
        if d[k] == max(a):
            print(k, d[k])
            i+=1
    a.remove(max(a))