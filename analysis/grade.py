import numpy as np

def check_pass_fail(marks, students):

    result = np.where(np.any(marks< 40, axis = 1), "Fail", "Pass")
    return students, result

def grade_distribution(marks):

    average = np.average(marks, axis= 1)
    check = (
        average >= 80, 
        (60 <= average) & (average < 80),
        (40 <= average) & (average < 60),
        (20 <= average) & (average < 40),
        (0 <= average) & (average <  20), 
        )
    grades = ["A", "B", "C", "D", "F"]
    result = np.select(check, grades, default="Unkonwn")
    return result
