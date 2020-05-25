#python program to reverse a given number
n=int(input("Enter number:\t"))
rev = 0
#does the  required operation
while(n>0):
        dig=n%10 #removes end digits of value
        rev=rev*10+dig#add the value to before value
        n=n//10
print("Reverse of the number:",rev)
