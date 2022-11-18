num = int(input())
mlist = []
for i in range(num):
    n = int(input())
    if (n % 10) < 9:
        n = n//10
        mlist.append(n)
    else:
        n = n//10 + 1
        mlist.append(n)
print(*mlist, sep='\n')
