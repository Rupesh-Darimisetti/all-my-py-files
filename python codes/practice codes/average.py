#This program is used to print average of Numbers in a given list

#Here is source of the python program to Calculate the averageof Numbers in a Given List.
n=int(input("Enter the number of elements to be intrested:"))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
    avg=sum(a)/n
    print("Average of elements in the list",round(avg,2))
