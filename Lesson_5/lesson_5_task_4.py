with open('lesson_5_task_4_input.txt', 'r') as file:
    my_file = file.readlines()
with open('lesson_5_task_4_output.txt', 'w', encoding='utf_8') as new_file:
    for line in my_file:
        if 'One' in line:
            line = line.replace('One', 'Один')
        elif 'Two' in line:
            line = line.replace('Two', 'Два')
        elif 'Three' in line:
            line = line.replace('Three', 'Три')
        elif 'Four' in line:
            line = line.replace('Four', 'Четыре')
        new_file.write(line)
