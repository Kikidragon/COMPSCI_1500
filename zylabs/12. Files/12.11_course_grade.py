name = input()
f = open(str(name))
#split by tabs and use the last 3 indexes to find avg
#if certain amount append letter grade
#print averages at teh bottom

file = f.readlines()
w = open('report.txt', 'w')
mid1 = 0
mid2 = 0
final = 0
count = 0
for line in file:
    line = line[:-1]
    count += 1
    x = line.split('\t')
    # for j in x:
    #     j = j.strip('\n')
    t1 = int(x[2])
    mid1 += t1
    t2 = int(x[3])
    mid2 += t2
    t3 = int(x[4])
    final += t3
    # t3 = t3[:2]
    # t3 = int(t3)
    avg = (t1+t2+t3)/3
    if avg > 90:
        grade = 'A'
    elif 80 < avg < 90:
        grade = 'B'
    elif 70 < avg < 80:
        grade = 'C'
    elif 60 < avg < 70:
        grade = 'D'
    else:
        grade = 'F'
    x.append(grade)
    # print(x)
    y = '\t'.join(x)
    w.write(y)
    w.write('\n')

w.write('\n')
w.write('Averages: midterm1 {:.2f}, midterm2 {:.2f}, final {:.2f}'.format(mid1/count, mid2/count, final/count))
w.write('\n')
f.close()
w.close()

