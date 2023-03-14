num = int(input("Enter a number to be checked "))
if num > 1:
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            print("{0} Not a prime Number ".format(num))
            break
    else:
        print("{0} is a Prime Number".format(num))
else:
    print("{0} is not a prime number ".format(num))
