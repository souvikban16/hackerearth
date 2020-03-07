#well be using recursion

def fact(a):
	if a!=1:
		return a*fact(a-1)
	else:
		return 1

def main():
	a=int(input())
	print(fact(a))

main()
