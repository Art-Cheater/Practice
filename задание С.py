a = int(input())

for i in range(a):
    n = int(input())

    if n % 2050 != 0:
        print(-1)
    else:
        b = 0
        while n > 0:
            c = len(str(n))-4
            e = 2050 * (10**c)

            if n-e < 0:
                c = c-1
                e = 2050 * (10 ** c)
            n = n-e
            b = b+1
        print(b)
