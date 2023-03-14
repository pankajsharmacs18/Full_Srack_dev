line1 = int(input("Enter 1st line "))
line2 = int(input("Enter 2nd line "))
line3 = int(input("Enter 3rd line "))

s = (line1 + line2 + line3) / 2
area = (s * (s - line1) * (s - line2) * (s - line3)) ** .5

print("Area of triangle is : {0:.2f} ".format(area))
