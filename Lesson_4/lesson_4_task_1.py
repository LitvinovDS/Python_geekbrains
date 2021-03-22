def payroll_calc(hours, salary_per_hour, prize):
    return hours*salary_per_hour + prize


from sys import argv
hours, salary_per_hour, prize = map(int, argv[1:])
print('Your salary is: ', payroll_calc(hours, salary_per_hour, prize))
