num = int(input("Enter a number"))

rev = 0
temp=num
while num != 0:
    rev = rev * 10 + num % 10
    num = num // 10
if rev==temp:
    print("Entered Number is palindrome ")
else:
    print("Not a palindrome")
