#
class emp:
    def __init__(self,name,age,school,college,job):
        self.name=name
        self.age=age
        self.school=school
        self.college=college
        self.job=job
    def Employee(self):
        if self.age<=15:
            return "name:{} age:{} school:{}".format(self.name,self.age,
                                                     self.school)
        else:
            return "name:{} age:{} colledge:{} job:{}".format(self.name,
                                self.age,self.college,self.job)

name=input('Name:')
age=int(input('age:'))
school=input('school:')
college=input('College:')
job=input('JOB:')
if age==18:
    print('Eligible for voter ID')
    print('Eligible for pan card')
    print('Eligible for licence to vehicles')

emp_1=emp(name,age,school,college,job)
print(emp_1.Employee())
