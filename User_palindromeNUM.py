n=int(input("enter the number"))
num=n
reverse=0
while n>0:
	a=n%10
	reverse=(reverse*10)+a
	n=n//10
if reverse==num:
	print('palindrome',reverse)
else:
	print('not a palindrome',reverse)