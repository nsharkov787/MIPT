with open('input.txt', 'r', encoding='utf-8') as f:
    d = f.read()
    c = 0
    for i in d:
         if i in '.!?':
             c = c + 1
print(c)
