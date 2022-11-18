t = (int(input()))
for i in range(t):
    p, h = sorted(input()), input()
    for i in range(len(h) - len(p) + 1):
        if sorted(h[i:i+len(p)]) == p:
            print('YES')
            break
    else:
        print('NO')
