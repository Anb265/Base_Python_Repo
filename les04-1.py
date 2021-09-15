from sys import argv
file_name, output_in_hours, rate_per_hour, bonus = argv

def fun_salary(argv):
    salary = int(argv[1]) * int(argv[2]) + int(argv[3])
    print(salary)

fun_salary(argv)