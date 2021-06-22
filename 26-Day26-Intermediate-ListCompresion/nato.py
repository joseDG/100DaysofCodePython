


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score" : [56, 78, 90]
}

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)


