for _ in range(int(input())):
    n, k = map(int, input().split())
    l = sorted(map(int, input().split()))
    c, ans = 0, 0
    for i in l[::-1]:
        if i <= c: break
        ans += 1
        c += n - i
    print(ans)