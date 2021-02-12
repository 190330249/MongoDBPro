class Student:

    def __init__(self, id, fname, lname, course, year, gpa, university, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.course = course
        self.year = year
        self.gpa = gpa
        self.university = university
        self.email = fname + lname + "@gmail.com"
        self.mobile = mobile

    def Student_info(self):
        print('Name:', self.fname, self.lname)
        print('ID Number:', self.id)
        print('Course:', self.course)
        print('Year:', self.year)
        print('GPA:', self.gpa)
        print('University:', self.university)
        print('Email ID:', self.email)
        print('Mobile Number:', self.mobile)

    def getYear(self):
        return (self.year)

    def getName(self):
        return self.fname + ' ' + self.lname

    def getID(self):
        return (self.id)

    def getMobileNo(self):
        return (self.mobile)

    def getEmail(self):
        return (self.email)

    def getUniversity(self):
        return (self.university)

    def getCourse(self):
        return (self.course)

    def getGPA(self):
        return (self.gpa)

    def getFname(self):
        return (self.fname)

    def getLname(self):
        return (self.lname)

    def setFname(self):
        a = input("Please enter the first name:")
        Student.setEmail(self, a, self.fname)
        self.fname = a
        print('First Name has been edited successfully')

    def setEmail(self, new, old):
        self.email = self.getEmail().replace(old, new)

    def setLname(self):
        a = input("Please enter the Last name:")
        Student.setEmail(self, a, self.lname)
        self.lname = a
        print('Last Name has been edited successfully')


def counter():
    global c
    print('Number of instances created =', c)


def StudentEntrySheet():
    global l
    global c
    while True:
        n = int(input("Do you want to enter the Student details:\n1.Yes\n2.No"))
        if n == 1:
            id = int(input("Enter Students ID:"))
            fname = input("Enter Students First Name:")
            lname = input("Enter Students last Name:")
            course = input("Enter Students Course:")
            year = int(input("Enter the Year of joining:"))
            gpa = float(input("Enter Students GPA:"))
            clg = input("Enter Students College:")
            no = int(input("Enter Students mobile number:"))
            l.append(Student(id, fname, lname, course, year, gpa, clg, no))
            c = c + 1

        else:
            break


def ModifyCheck():
    global c
    global l
    while True:
        n = int(input("Do you want to print all the details of the list that you have entered?\n1.Yes\n2.No"))
        if n == 1:
            for obj in l:
                print('\nID:', obj.getID(), '\nFirst Name:', obj.getFname(), '\nLast Name:', obj.getLname(),
                      '\nCourse:',
                      obj.getCourse(), '\nYear:', obj.getYear(), '\nGPA:', obj.getGPA(), '\nUniversity:',
                      obj.getUniversity(), '\nEmail:', obj.getEmail(), '\nMobile Number:', obj.getMobileNo())

        n = int(input("Do you want to change the First Name of a Student?\n1.Yes\n2.No"))
        if n == 1:
            while True:
                id = int(input("Enter the Student ID:"))
                flag = 0
                for i in l:
                    if i.getID() == id:
                        i.setFname()
                        flag = 1
                if flag == 0:
                    print("The ID you have entered is invalid!")
                    n = int(input("Do you want to retry?\n1.Yes\n2.No"))
                    if n == 2:
                        break
                if flag == 1:
                    break

        n = int(input("Do you want to change the Last Name of a Student?\n1.Yes\n2.No"))
        if n == 1:
            while True:
                id = int(input("Enter the Student ID:"))
                flag = 0
                for i in l:
                    if i.getID() == id:
                        i.setLname()
                        flag = 1
                if flag == 0:
                    print("The ID you have entered is invalid!")
                    n = int(input("Do you want to retry?\n1.Yes\n2.No"))
                    if n == 2:
                        break
                if flag == 1:
                    break

        n = int(input("Are you willing to exit?\n1.Yes\n2.No"))
        if n == 1:
            break


l = []
c = 0
n = int(input("Are you willing to enter Students details:\n1.Yes\n2.No\n"))
if n == 1:
    StudentEntrySheet()
counter()
n = int(input("Are you willing to modify or check Students details:\n1.Yes\n2.No\n"))
if n == 1:
    ModifyCheck()
print()
counter()
