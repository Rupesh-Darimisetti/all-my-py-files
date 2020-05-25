#python Object-Oriented programming
class emp:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first +'.'+ last +'@company.com'
        
    def fullname(self):
       return '{}{}'.format(self.first,self.last)
emp_1=emp('ram','krishna',50000)
emp_2=emp('pavan','kalyan',60000)
print(emp_1.fullname())
print(emp_2.fullname())    
