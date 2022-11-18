def foo(n):
	for i in range(2,int(n**0.5//1)+1):
		if n % i == 0 :return 0
	return 1
for q in range(int(input())):
	n=int(input());x=n+1
	while(not foo(x)):    x+=1
	y=x+n
	while(not foo(y)):    y+=1
	print(x*y)