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

    def count_probation(self):
        prob = []
        for i in self.roster:
            if i.get_gpa() < 2.0:
                prob.append(i)
            else:
                continue
        count = 0
        for student in prob:
            count += 1
        return count


if __name__ == "__main__":
    course = Course()
    course.add_student(Student('Henry', 'Cabot', 3.2))
    course.add_student(Student('Brenda', 'Stern', 1.1))
    course.add_student(Student('Lynda', 'Robison', 2.4))
    course.add_student(Student('Jane', 'Flynn', 1.8))

    prob_count = course.count_probation()
    print('Probation count:', prob_count)