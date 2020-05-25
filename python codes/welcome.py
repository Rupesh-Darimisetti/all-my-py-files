String="hello"
String2="welcome"
string="to python arithmethic"
print(String,String2,string)

print("Enter numbers")
a=input()
b=input()
print('a:Addition')
print('b:Subtraction')
print('c:Multiplication')
print('d:Division')
print("Enter your choise for operation")
abc=input()
def dict(abc,a,b):
    return{
        "a": lambda: a + b ,
        "b": lambda: a - b,
        "c": lambda: a * b,
        "d": lambda: a / b
        }.get(abc,lambda:"Invalid option choosen by you")()

