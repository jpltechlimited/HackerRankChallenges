def find_average(studentMarks, query):
    marks = studentMarks[query]
    return sum(marks) / len(marks)

if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    query_name = 'Harsh'
    student_marks = {'Harsh': [25.0, 26.5, 28.0], 'Anurag': [26.0, 28.0, 30.0]}
    average = find_average(student_marks, query_name)
    print("%.2f" % average)