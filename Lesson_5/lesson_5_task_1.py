with open('lesson_5_task_1_testfile.txt', 'w') as testfile:
    while True:
        user_text = input('Введите текст ')
        if user_text == '':
            break
        testfile.write(user_text + '\n')
print('Работа программы окончена, проверьте файл.')