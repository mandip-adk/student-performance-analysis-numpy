import numpy as np

#Subjects and Students
def generate_student_data():
    subjects = np.array(["Maths","Science", "Computer", "Nepali","English"])
    students = np.array(["Student1", "Student2","Student3","Student4","Student5"])
    marks = np.random.randint(0, 101, size=(5,5))

    return subjects, students, marks


