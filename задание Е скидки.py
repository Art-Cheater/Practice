n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
q = [int(x) for x in input().split()]
a.sort()
s = sum(a)
for i in q:
    print(s-a[-i])
