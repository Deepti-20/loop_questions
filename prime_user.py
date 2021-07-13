n=int(input("enter the number :"))
t=0
i=2
while i<n:
	if n % i == 0:
		# print(i)
		t+=1
	i+=1
if t==0:
	print("prime number")
else:
	print("not prime number")