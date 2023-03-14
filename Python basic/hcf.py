def hcfORgcd(num1, num2):
    hcf = 1
    for i in range(2, (num1 if num1 < num2 else num2) +1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf


num1 = int(input("Enter 1st number!"))
num2 = int(input("Enter 2nd numebr !"))
print("HCF of {0} and {1} is {2} ".format(num1, num2, hcfORgcd(num1, num2)))
