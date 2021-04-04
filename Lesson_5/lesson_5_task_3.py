with open('lesson_5_task_3_testfile.txt', 'r', encoding='utf_8') as testfile:
    all_staff = testfile.readlines()
average_income = 0
for i in range(len(all_staff)):
    employee = all_staff[i].split(' ')
    if int(employee[1]) < 20000:
        print(employee[0])
    average_income += int(employee[1])
print('Средний доход: ', round(average_income/len(all_staff)))
