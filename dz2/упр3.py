s = input()
# a = {"AHIMOTUVWXYEJSZ"}
b = s[::-1]
flag1 = 0
flag2 = 0
flag3 = 0
# ALJA
symbols = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1', '8': '8','E': '3', 'J': 'L', 'S': '2', 'Z': '5','3': 'E', 'L': 'J', '2': 'S', '5': 'Z'}
for i in range(len(s)):
    if s[i] not in "AHIMOTUVWXYEJSZ3L25":
        flag3 = 1
        flag1 = 1
if flag3 == 0:
    for i in range(len(s)):
        if s[i] != symbols[s[-i - 1]]:
            flag1 = 1
if b != s: flag2 = 1
if flag1 == 0 and flag2 == 0:
    print(s, 'is a mirrored string.')
if flag1 == 1 and flag2 == 0:
    print(s, 'is a mirrored palindrome')
if flag1 == 0 and flag2 == 1:
    print(s, 'is a regular palindrome.')
if flag1 == 1 and flag2 == 1:
    print(s, "is not a palindrome")





