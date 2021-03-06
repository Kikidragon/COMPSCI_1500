class Student:
    def __init__(self, first, last, gpa):
        self.first = first  # first name
        self.last = last    # last name
        self.gpa = gpa      # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last


class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def find_student_highest_gpa(self):
        maxx = 0.0
        for i in self.roster:
            # print(type(i.get_gpa()))
            # print(type(maxx))
            if i.get_gpa() > maxx:
                maxx = i.get_gpa()
            else:
                continue
        for i in self.roster:
            if i.get_gpa() == maxx:
                return i


if __name__ == "__main__":
    course = Course()
    course.add_student(Student('Henry', 'Nguyen', 3.5))
    course.add_student(Student('Brenda', 'Stern', 2.0))
    course.add_student(Student('Lynda', 'Robison', 3.2))
    course.add_student(Student('Sonya', 'King', 3.9))

    student = course.find_student_highest_gpa()
    print('Top student:', student.first, student.last, '( GPA:', student.gpa, ')')
