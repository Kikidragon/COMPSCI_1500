class Student:
    def __init__(self, first, last, gpa):
        self.first = first  # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

    def get_first(self):
        return self.first


class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def print_roster(self):
        count = 0
        for i in self.roster:
            count += 1
            print("{} {} ( GPA: {} )".format(i.get_first(), i.get_last(), i.get_gpa()))
        print("Students: {}".format(count))


if __name__ == "__main__":
    course = Course()
    course.add_student(Student('Henry', 'Cabot', 3.5))
    course.add_student(Student('Brenda', 'Stern', 2.0))
    course.add_student(Student('Jane', 'Flynn', 3.9))
    course.add_student(Student('Lynda', 'Robison', 3.2))

    course.print_roster()