n = int(input())
s = str(input())
i = 0
while i <= len(s):
    if s[i] == '?':
        s[i] = 'A'
    i += 1
    print(s)
