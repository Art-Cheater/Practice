n = int(input())
if n < 3:
    print(-1)
else:
    print(*range(n, 0, -1))
