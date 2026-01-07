class Student:
    def __init__(self,id,name,dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.course = []
        self.marks = []
    def save_course(self):
        n = input(f"Enter the course the student {self.name} registered: ").split()
        arr = []
        for i in n:
            if i not in self.course:
                self.course.append(i)
        print("course = ",self.course)
    
    def save_mark(self,courses):
        for _ in self.course:
            for c in courses:
                if _ == c.course_id:
                    print(f"Enter mark for student {self.name} of course {c.course_name}: ")
                    n = float(input())
                    while (n > 10.0 or n<0):
                        print("Mark invalid, enter valid mark")
                        print(f"Enter mark for student {self.name} of course {c.course_name}: ")
                        n = float(input())
                    else:
                        self.marks.append(n)
        
    def do_homework(self):
        print(f"{self.name} is doing homework")

    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.name}, DOB: {self.dob}"
    
class mark:
    def __init__(self):
        self.student_id = []
        self.course_id = ""
        self.mark = []

    def __str__(self):
        return f"Student ID: {self.student_id}, Course ID: {self.course_id}, Mark: {self.mark}"

class Course:
    def __init__(self,course_id,course_name):
        self.course_id = course_id
        self.course_name = course_name
    
    def input(self):
        
        self.course_id,self.course_name = input("Id and name of the course (separated by spaces): ").split()
        

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}"


print('''                ===Database of student====\n
Note:
    *Type data for student
- Type id, name and DoB of the student at same line. For example: 1 abc 01/01/1990
- When input type id of student, length of id must be more than zero and less than 8 digits
- Date of birth has format: dd/mm/yyyy
- If the course that student registered does not have in school, it cant be displayed and user can add more than one course and have a space among 2 courses. For example: 101 102
- Mark of student must be in range 0 to 10, otherwise mark not be allowed
    *Type data for courses
- Maxium length for name of courses is 9 and have at least 1 digit
- Type id and name of course in the same line and has a space between them (101 math)

      ''')
n = int(input("Enter number of students:"))
id_list = [str(i) for i in range(0,10)]
name_list = ["a","b","c","d","e","f","g","h","i","j"]
date = "1/1/2000"

student_list = []
sorted_list = []
courses_list = []

for _ in range(n):
    check_id= True
    num = [str(i) for i in range(0,10)]
    check_name = True
    check_DoB = True
    a= input("Id,name,DoB of student number "+str(_+1) + ":").split()
    while (len(a))!=3:
        print("Invalid input")
        a= input("Id,name,DoB of student number "+str(_+1) + ":").split()
    else:
        id,name,DoB = a
    while check_id:
        id_lst = []
        for _ in student_list:
            id_lst.append(_.id)
        if id in id_lst:
            print("Id exist, enter another!")
            id = input("Id: ")
        elif len(id) <= 0 or len(id) > 8:
            print("Id too short or too long, enter another!")
            id = input("Id: ")
        else:
            check_id = False
        
    while check_name:
        if len(name) <=0 or len(name)>9:
            print("Student's name too short or too long, name of student in range 1 to 9 digits")
            name = input("Name:")
        
        else:
            check_digits = True
            for i in name:
                if i in num:
                    check_digits = False
                    print("Invalid name, name does not contain number")
                    name = input("Name: ")
                    break
            if check_digits:
 
                check_name = False
    
    while check_DoB:
        if len(DoB.split("/")) != 3:
            print("Invalid date of birth format!")
            DoB = input("Type correct student's DoB with format (dd/mm/yyyy): ")
            continue
        else:
            d,m,y = map(int,DoB.split("/"))

            if (m == 2):
                if y%400 == 0:
                        if (d > 29 or d <= 0):
                            print("Invalid day!")
                        else:
                            check_DoB = False
                elif y%4 == 0 and y%100 !=0:
                    if (d>29 or d<=0):
                        print("Invalid day!")
                    else:
                        check_DoB = False
                else:
                    if (d > 28 or d<=0 ):
                        print("Invalid day!")
                    else:
                        check_DoB = False
                            
                
            else:
                if (m <=7):
                    if m%2 == 1:
                        if (d > 31 or d <=0):
                            print("invalid day!")
                                    
                        else:
                            check_DoB = False

                    if m%2 == 0:
                        if (d>30 or d<=0) :
                            print("Invalid day!")  
                        else:
                            check_DoB = False        
                elif (m > 7 and m < 13):
                    if m%2 == 1:
                        if (d>30 or d<=0):
                            print("Invalid day!")
                        else:
                            check_DoB = False
                    elif m%2 == 0:
                        if (d>31 or d < 1):
                            print("Invalid day!")
                        else:
                            check_DoB = False
                else:
                    print("Invalid month!!")
            if check_DoB:
                DoB = input("Type correct student's DoB with format (dd/mm/yyyy): ")
    if not check_id and not check_name and not check_DoB:
        s = Student(id,name,DoB)
        student_list.append(s)

for _ in student_list:
    print(_)
m = int(input("Enter number of courses:"))
print()
for i in range(m):
    b = Course("", "")
    b.input()
    courses_list.append(b)
    print()


for _ in courses_list:
    print(_)

print()
for _ in student_list:
    print(_)
    _.save_course()
    _.save_mark(courses_list)
    print()

for _ in student_list:
    print(f"Student: {_.name}")

    for i in range(len(_.marks)):
        print(f"Course: {_.course[i]}, mark: {_.marks[i]}")
        print()

course_mark = []
for p in courses_list:
    c = mark()
    for _ in student_list:
        for i in range(len(_.course)):
            if _.course[i] == p.course_id:
                c.student_id.append(_.id)
                c.course_id = _.course[i]
                c.mark.append(_.marks[i])
    course_mark.append(c)
sort = []
for _ in course_mark:

    c = mark()
    for i in range(len(_.mark)):
        check = True
        if i == 0:
            c.course_id = _.course_id
            c.mark.append(_.mark[i])
            c.student_id.append(_.student_id[i])
        else:
            for j in range(len(c.student_id)):
                if check:
                    if (_.mark[i] >= c.mark[j]):
                        std_x = c.student_id[j]
                        mark_x = c.mark[j]

                        c.mark[j] = _.mark[i]
                        c.student_id[j] = _.student_id[i]
                        check = False
                        for f in range(j+1,len(c.student_id)):

                            mark_y = c.mark[f]
                            c.mark[f] = mark_x
                            mark_x = mark_y

                            std_y = c.student_id[f]
                            c.student_id[f] = std_x
                            std_x = std_y
            if check:
                mark_x = _.mark[i]
                std_x = _.student_id[i]

            c.mark.append(mark_x)
            c.student_id.append(std_x)

    sort.append(c)


print("      Tên   Môn học   Điểm   Xếp thứ")
for _ in sort:
    for i in courses_list:
        if i.course_id == _.course_id:
            course_name_idx = i.course_name
    
    for i in range(len(_.mark)):
        for j in student_list:
            if j.id == _.student_id[i]:
                space = " "
                for o in range(9-len(j.name)):
                    print(space,end = "")
                print(j.name,end = "")
                for o in range(10 - len(course_name_idx)):
                    print(space,end = "")
                
                print(course_name_idx,end = "")
                
                for o in range(7-len(str(_.mark[i]))):
                    print(space,end = "")
                
                print(str(_.mark[i]),end = "")
                
                for o in range(10- len(str(i+1))):
                    print(space,end = "")
                print(str(i+1))
    print()
        

    
