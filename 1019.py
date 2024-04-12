time = int(input())
divisor = 3600
for i in range(3):
    number = int(time // divisor)
    time = time % divisor
    if i < 2:
        print(f'{number}:',end='')
    else:
        print(number)
    divisor = divisor / 60
