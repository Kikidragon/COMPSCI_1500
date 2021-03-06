class Student:
    def __init__(self):
        self.name = "Louie"
        self.gpa = 1.0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_gpa(self, gpa):
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa


if __name__ == "__main__":
    initial_student = Student()
    print(initial_student.get_name(),'/', initial_student.get_gpa())

    initial_student.set_name('Felix')
    initial_student.set_gpa(3.7)
    print(initial_student.get_name(), '/', initial_student.get_gpa())
