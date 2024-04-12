employee_number = input()
number = f'NUMBER = {employee_number}'
worked_hours = int(input())
amount_per_hour = float(input())
salary = worked_hours * amount_per_hour
print(number)
print(f'SALARY = U$ {salary:.2f}')
