#program to check a perfect number
n=int(input("Enter any number: "))
sum1=0
for i in range(1,n):
    if(n%i==0):
        sum1=sum1+i
        print(sum1)
if(sum1==n):
    print("The number is a perfect number!")
else:
    print("The number isn't a perfect number!")
