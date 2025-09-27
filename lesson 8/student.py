class Student:
    school_name = "Digital school"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student_1 = Student( "alice",  15, "python")
student_2 = Student("bob", 17,  "javascript")
print(student_1.course)
print(student_2.course)