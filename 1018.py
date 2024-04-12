money = int(input())
my_list = [100, 50, 20, 10, 5, 2, 1]
i = 0
print(money)
while(i<7):
    divisor = int(my_list[i])
    last_money = money // divisor
    print(f"{last_money} nota(s) de R$ {my_list[i]},00")
    money = money % divisor
    i += 1
