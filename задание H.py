a, b, c, d = map(int, input().split())
if (a+b) >= c and (a+c) >= b and (c+b) >= a:
    if (a+b) == c or (a+c) == b or (c+b) == a:
        print('SEGMENT')
    else:
        print('TRIANGLE')
elif (a+b) >= d and (b+d) >= a and (a+d) >= b:
    if (a+b) == d or (b+d) == a or (a+d) == b:
        print('SEGMENT')
    else:
        print('TRIANGLE')
elif (a+d) >= c and (a+c) >= d and (c+d) >= a:
    if (a+d) == c or (a+c) == d or (c+d) == a:
        print('SEGMENT')
    else:
        print('TRIANGLE')
elif (b+c) >= d and (d+c) >= b and (d+b) >= c:
    if (b+c) == d or (d+c) == b or (d+b) == c:
        print('SEGMENT')
    else:
        print('TRIANGLE')
else:
    print('IMPOSSIBLE')