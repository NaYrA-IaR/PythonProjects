def fact(n):
	prod = 1
	for i in range(1,n+1):
		prod = prod*i
	return prod

n = input("Enter a number")
print(f"The factorial of {n} is {fact(n)}")