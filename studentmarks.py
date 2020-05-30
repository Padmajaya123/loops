student_name = 'rekha'

marks = {'John': 90, 'balaji': 55, 'geetha': 97,'rekha':82}

for i in marks:
    if i == student_name:
        print(marks[i])
        break
else:
    print('No entry')