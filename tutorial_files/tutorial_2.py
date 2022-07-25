# Class Variables apply to all instances of the class

class Student:
    
    # class variable added to the 'Student' class
    raise_amount = 1.34
    
    def __init__(self, first, last, major, dean_bucks):
        self.first = first
        self.last = last
        self.major = major
        self.email = first + '.' + last + "@greendale.edu"
        self.dean_bucks = dean_bucks

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    # access the class variable through the class
    def apply_dean


    # access the class variable through an instance of a class
    def apply_dean_bucks(self):
        self.dean_bucks = int(self.dean_bucks * self.raise_amount)





stu_1 = Student('Britta', 'Perry', 'Psychology', 50)
stu_2 = Student('Jeff', 'Winger', 'Independent Studies', 10000)
stu_3 = Student('Troy', 'Barnes', 'AC Repair', 700)
stu_4 = Student('Annie', 'Edison', 'Hospital Administration', 600)
stu_5 = Student('Abed', 'Nadir', 'Film Studies', 800)
stu_6 = Student('Shirley', 'Bennett', 'Business', 750)


print(stu_1.fullname())
print(Student.fullname(stu_1))






print(stu_1.dean_bucks)
stu_1.apply_dean_bucks()
print(stu_1.dean_bucks)