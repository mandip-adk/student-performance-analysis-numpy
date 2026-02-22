import numpy as np

from data.students_data import generate_student_data
from analysis.grade import check_pass_fail, grade_distribution
from analysis.statistics import average_per_student, subject_wise_average, top_scorer, lowest_scorer

subjects, students, marks = generate_student_data()

stu_average = average_per_student(marks)
paired= zip (students, stu_average)
print("--- Average Per Student ---")
for student, avg in paired:
    print(student, avg)

sub_average = subject_wise_average(marks)
paired = zip (subjects, sub_average)
print("--- Average Per Subject ---")
for sub, avg in paired:
    print (sub, avg)

top = top_scorer(marks, students)
print("--- Top Score Student ---")
print(top)

low = lowest_scorer(marks, students)
print("--- Lowest Score Student ---")
print(low)

student_result,check = check_pass_fail(marks, students)
paired = zip (student_result, check)
print("--- Pass/Fail ---")
for stu, check in paired:
    print(stu, check)

grade = grade_distribution(marks)
paired = zip (students, grade)
print("--- Grades ---")
for stu, g in paired:
    print(stu, g)

