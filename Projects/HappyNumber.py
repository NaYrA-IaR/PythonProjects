print("******Checking if the given number is a Happy Number or not******")

def sum_of_digit(n):
    sum=0
    while(n):
        r=n%10
        sum += r**2
        n=int(n/10)
    return sum

print("\n For example 7 is a Happy Number as: \n")
print("7 -> 7^2 = 49\n49 -> 4^2 + 9^2 = 97\n97 -> 9^2 + 7^2 = 130\n130 -> 1^2 + 3^2 + 0^2 = 10\n10 -> 1^2 + 0^2 = 1\n")
print("\nThe first 8 Happy Numbers are 1, 7, 10, 13, 19, 23, 28, 31")
conti = 'y'
while(conti is not 'n'):
    flag=0
    n=int(input("\nEnter a number to check if it's Happy Number or not: "))
    value = list()
    value.append(n)
    while(n is not 1):
        n = sum_of_digit(n)
        if n in value:
            flag=1
            break
        value.append(n)

    if flag is 1:
        print("\nNumber ain't a Happy Number")
    else:
        print("\n{} is a Happy Number.".format(value[0]))
    conti = input("\nEnter n to exit: ")
    conti.lower()

print("\n****************THANK YOU********************")