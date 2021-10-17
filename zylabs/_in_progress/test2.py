class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60
        return Duration(total_hours, total_minutes)

first_trip = Duration(2, 31)
second_trip = Duration(0, 53)

first_time = first_trip + second_trip
second_time = second_trip + second_trip

print(first_time.hours, first_time.minutes)
print(second_time.hours, second_time.minutes)