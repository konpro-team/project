for i in range(5,0,-1):
	for j in range(0,i):
		if(i%2)==1:
			print("*", end=" ")
		else:
			print("#", end=" ")
	print()