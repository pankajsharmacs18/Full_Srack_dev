def lcmCal(n1, n2, larger):
    if larger % n1 == 0 and larger % n2 == 0:
        return larger
    else:
        return lcmCal(n1, n2, larger + 1)


num1 = int(input("Enter 1st number "))
num2 = int(input("enter 2nd number "))
lcm = 1
if num1 % num2 == 0:
    lcm = num1
elif num2 % num1 == 0:
    lcm = num2
else:
    large = num1 if num1 > num2 else num2
    lcm = lcmCal(num1, num2, large)
    print(lcm)
print("LCM of {0} and {1} is {2} ".format(num1, num2, lcm))
