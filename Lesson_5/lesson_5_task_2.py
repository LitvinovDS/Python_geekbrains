with open('lesson_5_task_2_testfile.txt', 'r') as testfile:
    my_file = testfile.readlines()
    print('В файле ', len(my_file), ' строк')
    for i in range(len(my_file)):
        print(i+1, ' строка - ', len(my_file[i].split(' ')), 'слов')
