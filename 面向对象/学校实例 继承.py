class school(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print('为学员%s 办理注册手续'% stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print('雇佣新员工%s'%staff_obj.name)
        self.staffs.append(staff_obj)

class schoolmember(object):
    def __init__(self,name,age,sex):
        self.name =name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class teacher(schoolmember):
    def __init__(self,name,age ,sex,salary,course):
        super(teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
            """info of teacher"""
            name:%s
            age:%s
            sex:%s
            salary:%s
            course:%s
        '''%(self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print('%s is teaching course:%s'%(self.name,self.course))



class students(schoolmember):
    def __init__(self,name,age ,sex,stu_id,grade):
        super(students,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
            """info of students"""
            name:%s
            age:%s
            sex:%s
            salary:%s
            course:%s
        '''%(self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay_tution(self,amount):
        print('%s has paid tution for ￥%s'%(self.name,amount))


school = school('young bird','西三环')
t1 = teacher('liangyawang',18,'man',15000,'python')
t1.tell()
t1.teach()
s1 = students('liangjing',17,'woman',1,9)
s1.tell()
school.hire(t1)
school.enroll(s1)
print(school.students)
print(school.staffs)
school.staffs[0].teach()

for stu in school.students:
    stu.pay_tution(2000)