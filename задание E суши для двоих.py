t=int(input())
a=list(map(int,input().split()))
c=1
m=0
m1=0
for i in range(1,t):
    if a[i]==a[i-1]:
        c+=1
    else:
        m1=c
        c=1
    m=max(m,min(m1,c))
print(2*m)