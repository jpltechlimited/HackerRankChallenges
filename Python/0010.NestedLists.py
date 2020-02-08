class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def second_lowest_grade(students):
    students.sort(key=lambda x: x.grade)
    lowestGradeStudent = students[0]
    filtered = list(filter(lambda x: x.grade != lowestGradeStudent.grade, students))
    lowestGradeStudent = filtered[0]
    filtered.sort(key=lambda x: x.name)
    for student in filtered:
        if student.grade == lowestGradeStudent.grade:
            print(student.name)

if __name__ == '__main__':
    python_students = []    
    python_students = [Student('Harsh',20), Student('Beria', 20), Student('Varun', 19), Student('Kakunami', 19), Student('Vikas', 21)]

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     python_students.append(Student(name, score))
    
    second_lowest_grade(python_students)
