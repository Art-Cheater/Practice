q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    print(s[n] - s[n-1])