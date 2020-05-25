#program to check a year is a leap year or not
year=int(input("Enter Year to be checked: "))#input year to be checked
if(year%4==0 and year%100!=0 or year%400==0):#condition for given program i.e. a leap year or not
#if condition is true prints leap year or print it is not a leap year
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
