class diplamo:
    def __init__(self,name,fathername,sem):
        self.name=name
        self.fathername=fathername
        self.sem=sem
    def tab(self):
        return "Name\t\t: {}\nFather Name\t: {}\nSEMESTER\t: {}".format(self.name,self.fathername,self.sem)
sem=int(input('Semester:'))
emp1=diplamo("Rupesh Darimisetti","Ganesh Darimisetti",sem)
print(emp1.tab())

if sem==1:
    print("101-English\t\t\t:")
    print("102-Mathematics-I\t\t:")
    print("103-Physics\t\t\t:")
    print("104-Chemistry\t\t\t:")
    print("105-Engineering Mechanics\t:")
    print("106-WorkshopTechnology\t\t:")
if sem==3:
    print("301-Mathemathics-II\t\t\t:")
    print("302-Strength Of Materials\t:")
    print("303-Thermal Engineering-I\t:")
    print("304-Production Technology-I\t")
    print("305-Basic Electrical Engineering:")
    print("306")
if sem==4:
    print("401-Engineering Materials\t:")
    print("402-hydraulics\t\t\t:")
    print("403-Thermal Engineering-II\t:")
    print("404-Production Technology\t:")
    print("405-Design of Machine Elements\t:")
