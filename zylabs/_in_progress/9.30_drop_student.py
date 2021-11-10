# FIXME UNFINISHED
class Student:
    def __init__(self, first, last, gpa):
        self.first = first  # first name
        self.last = last    # last name
        self.gpa = gpa      # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

    def to_string(self):
        return self.first + ' ' + self.last + ' (GPA: ' + str(self.gpa) + ')'

class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def drop_student(self, student):
        for i in self.roster:
            x = i.get_last
            if x == student:
                self.roster.remove(i)
            # FIXME
            # x = i.get_last
            # if x == student:
            #     if student in i:
            #         self.roster.remove(i)
        #
            # if student in i:
            #     self.roster.remove(i)

        # if student in self.roster:
        #     self.roster.remove()
            # use get_last() to specify student var is a last name

    def add_student(self, student):
        self.roster.append(student)

    def count_students(self):
        return len(self.roster)


if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry', 'Nguyen', 3.5))
    course.add_student(Student('Brenda', 'Stern', 2.0))
    course.add_student(Student('Lynda', 'Robinson', 3.2))
    course.add_student(Student('Sonya', 'King', 3.9))

    print('Course size:', course.count_students(), 'students')
    course.drop_student('Stern')
    print('Course size after drop:', course.count_students(), 'students')