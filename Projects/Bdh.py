print("Program To print The binary, octal, decimal, hexadecimal from 1 to given number.")


def print_formatted(number):
    
    width = len(bin(number))
    for i in range(1,number+1):
        for base in 'doXb':
            print("{0:<{width}{base}}".format(i , width = width-1 , base = base),end='')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)