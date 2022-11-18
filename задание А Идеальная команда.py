q=int(input())
for i in range(q):
    c,m,x=map(int,input().split())
    print(min(c,(c+m+x)//3,m))