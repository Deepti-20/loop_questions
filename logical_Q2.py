a=int(input("enter the number--"))
b=int(input("enter the number--"))
while a%b!=0:
	rem=a%b
	a=b
	b=rem
print(rem)