sum_grade = 0
total = 0
grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for i in range(20):
    subject, grade, letter = input().split()
    if letter != 'P':
        grade = float(grade)
        total += grade
        sum_grade += grade * grade_dict[letter]

print(sum_grade / total)