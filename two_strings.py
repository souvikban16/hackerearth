for i in range(int(input())):
	a,b=input().split(" ")
	if(len(a)==len(b)):
		seta=list(map(str,a))
		setb=list(map(str,b))

		for i in seta:
			if i in setb:
				setb.remove(i)
			else:
				print("NO")
				break
		if setb==[]:
			print("YES")
	else:
		print("NO")