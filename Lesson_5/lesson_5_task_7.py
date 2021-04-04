import json

with open('lesson_5_task_7_company.txt', 'r', encoding='utf-8') as companies_file:
    companies = companies_file.readlines()

average_profit, num_com = 0, 0
my_dict = {}
for company in companies:
    company = company.split()
    profit = int(company[2]) - int(company[3])
    my_dict[company[0]] = profit
    if profit >=0:
        average_profit += profit
        num_com += 1
average_profit = round(average_profit/num_com)
my_dict['average_profit'] = average_profit

with open('lesson_5_task_7_out.json', 'w') as out_json:
    json.dump(my_dict, out_json)

with open('lesson_5_task_7_out.json', 'r') as out_json:
    print(json.load(out_json))
