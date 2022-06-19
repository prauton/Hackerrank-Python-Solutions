if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = 0
    z = student_marks[query_name]
    y = len(z)
    for i in range(y):
        marks = marks + z[i]
    x = marks/y
    f = "{:.2f}".format(x)
    print(f)
