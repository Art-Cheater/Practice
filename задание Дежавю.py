tests = int(input())

for tests in range(tests):
    s = input()

    i = 0
    result = False
    while i <= len(s) // 2:
        if s[i] != 'a':
            result = True
            print("YES")
            print(s + 'a')
            break
        if s[len(s) - i - 1] != 'a':
            result = True
            print('YES')
            print('a' + s)
            break
        i += 1
    if not result:
        print('NO')

