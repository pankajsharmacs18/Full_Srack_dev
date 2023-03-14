num = int(input("Enter a number"))

temp = 0
while num != 0:
    temp = temp * 10 + num % 10
    num = num // 10

print("reversed number  {0}".format(temp))
