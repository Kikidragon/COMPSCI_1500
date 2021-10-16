hours = int(input())
minutes = int(input())
seconds = int(input())

min2 = hours * 60
sec = (min2 + minutes) * 60
sec_final = sec + seconds

print("Seconds:", sec_final)