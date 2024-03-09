import random
names = ["alex","mert","eren","frodo"]
student_scores = {student:random.randint(1,100) for student in names}
passed_student = {student:score for (student,score) in student_scores.items() if score>=60}

print(student_scores)
print(passed_student)

numbers = [1,2,3]
new_numbers = [n*2 for n in range(1,5)]
print(new_numbers)

names = ["Alex","Mert","elenore",]
new_names = [n.upper() for n in names if len(n)<5]


print(new_names)