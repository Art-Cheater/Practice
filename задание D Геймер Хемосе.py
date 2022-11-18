t = int(input())
ans = ''
for i in range(t):
    n, h = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    a, b = arr[0], arr[1]
    b += a
    ans += str(h//b*2 + (h % b > 0) + (h % b > a))+'\n'
print(ans)
