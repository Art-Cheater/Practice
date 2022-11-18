tests = int(input())

for test in range(tests):
    n = int(input())

    if n % 2050 != 0:
        print(-1)
    else:
        numbers_count = 0
        while n > 0:
            k = len(str(n)) - 4
            q = 2050 * (10 ** k)

            if n - q < 0:
                k -= 1
                q = 2050 * (10 ** k)

            n = n - q
            numbers_count += 1
        print(numbers_count)