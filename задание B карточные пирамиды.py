for _ in range(int(input())):
	n=int(input())
	ans=0
	while n>1:
		ans+=1
		h=int((-1+(1+24*n)**0.5)/6)
		s=(3*(h**2)+h)//2
		n-=s
	print(ans)