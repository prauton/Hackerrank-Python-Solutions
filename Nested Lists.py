if __name__ == '__main__':
    list2 = []
    marks =[]
    for _ in range(int(input())):
        l= []
        l.append(input())
        score = float(input())
        l.append(score)
        list2.append(l)
        marks.append(score)
    marks.sort()
    z = marks[0]
    res_name =[]
    for x in marks:
        if x>z:
            res_val = x
            break
    for i in range(len(list2)):
        if res_val in list2[i]:
            res_name.append(list2[i][0])
    res_name.sort()
    for i in res_name:
        print(i)
