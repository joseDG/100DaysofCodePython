names = ["Alex", "Beth", "Carolina", "Dave", "Elanor", "Freddy", "jose"]
import random 

students_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)