time = int(input())
my_list1 = [365, 30, 1]
my_list2 = ["ano(s)", "mes(es)", "dia(s)"]
for i in range(3):
    divisor = int(my_list1[i])
    number = time // divisor
    print(f'{number} {my_list2[i]}')
    time = time % divisor
