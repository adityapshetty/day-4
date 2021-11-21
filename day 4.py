class people:
    def __init__(self,name,gender,age,work,salary):
        self.name=name;
        self.gender=gender;
        self.age=age;
        self.work=work;
        self.salary=salary;
    def info(self):
        print(f"name={self.name} \ngender={self.gender} \nage={self.age} \nwork={self.work} \nsalary={self.salary} \n \n")

student=people("raju","male",19,"student",0)
teacher=people("rahul","male",38,"teacher",60000)
student.info()
teacher.info()
