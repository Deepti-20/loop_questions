i=1
k=1
while i<=5:
	j=0
	while j<i:
		print(k,end=" ")
		j=j+1+k
		k=k+1+k
	print()
	i=i+1


# :-) Out --1
#           3
#           7
#           15
#           31