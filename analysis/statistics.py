import numpy as np


def average_per_student(marks):
    stu_avg = np.mean(marks, axis= 1)
    return stu_avg

def subject_wise_average(marks):
    sub_avg = np.mean(marks, axis= 0)
    return sub_avg

def top_scorer(marks, students):
    total = np.sum(marks, axis=1)
    index= np.argmax(total)
    return students[index]

def lowest_scorer(marks, students):
    total = np.sum(marks, axis=1)
    index = np.argmin(total)
    return students[index]
