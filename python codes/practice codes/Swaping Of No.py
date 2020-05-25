#here is  the source code of python program to exchange values of two numbers withoutusing a temporary variable.
a=int(input("Enter value of first variable:\t"))
b=int(input("Enter value of second variable:\t"))
a=a+b
b=a-b
a=a-b
print("a is:\t",a,"\nb is:\t",b)
