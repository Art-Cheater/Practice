m=int(input())
for t in range(m):
	n=int(input())
	a=list(map(int,input().split()))
	a.sort()
	f=0
	if sum(a)%2==0:
		f=1
	else:
		for i in range(n-1):
			if abs(a[i]-a[i+1])==1:
				f=1
				break
	print("YES" if f==1 else "NO")