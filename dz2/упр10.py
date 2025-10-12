# with open('input.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
text = open('input.txt', encoding='utf-8').read()
glasn = 'аеёиоуыэюяaeiouy'
a = []
i = 0
while i < len(text):
    a.append(text[i])
    if text[i].lower() in glasn:
        if i == 0 or text[i - 1].lower() not in glasn:
            if text[i].isupper():
                a.append('С' + text[i].upper())
            else:
                a.append('с' + text[i].lower())
    i += 1
output_text = ''.join(a)
print(output_text)