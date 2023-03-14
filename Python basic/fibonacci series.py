num = int(input("Enter range of fibonacci series "))
n1=0
n2 =1
print(n1,n2,end=" ")
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
for i in range(num + 1):
    n3 =n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
