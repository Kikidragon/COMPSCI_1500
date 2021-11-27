class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    if name in info:
        return info[name]
    else:
        raise StudentInfoError("Student ID not found for {}".format(name))


def find_name(ID, info):
    for key, value in info.items():
        if value == ID:
            return key
    else:
        raise StudentInfoError("Student name not found for {}".format(ID))


if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan': 'rebradshaw835',
        'Ryley': 'rbarber894',
        'Peyton': 'pstott885',
        'Tyrese': 'tmayo945',
        'Caius': 'ccharlton329'
    }

    userChoice = input()  # Read search option from user. 0: find_ID(), 1: find_name()

    #  find_ID() and find_name() may throw an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    # if userChoice == "0":
    #     name = input()
    #     result = find_ID(name, student_info)
    # else:
    #     ID = input()
    #     result = find_name(ID, student_info)
    # print(result)
    if userChoice == "0":
        name = input()
        try:
            result = find_ID(name, student_info)
            print(result)
        except StudentInfoError:
            print("Student ID not found for {}".format(name))
    else:
        ID = input()
        try:
            result = find_name(ID, student_info)
            print(result)
        except StudentInfoError:
            print("Student name not found for {}".format(ID))

