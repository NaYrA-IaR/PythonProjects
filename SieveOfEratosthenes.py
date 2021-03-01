print("****This programme shows all the primes between 2 and a given number(n)****")
n=int(input("Value of n: "))
val=[True for i in range(n+1)]
p=2
while(p*p<n):
    for i in range(p*p,n+1,p):
        val[i]=False
    for j in range(p+1,n+1):
        if(val[j]==True):
            p=j
            break
for i in range(2,n+1):
    if(val[i]==True):
        print(i)