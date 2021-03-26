## FACTORIAL USING RECURSION

def fact(n):
    prod = 1
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("Enter a number: "))
print(f"The Factorial of {n} is {fact(n)}")