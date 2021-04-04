with open('lesson_5_task_6_file.txt', 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()

subject_dict = {}
for line in lines:
    subject = line.split()
    subject_dict[subject[0]] = sum([int(i[:i.find('(')]) for i in subject if ':' not in i])
print(subject_dict)
