import math
my_list = input().split(" ")
a = float(my_list[0])
b = float(my_list[1])
c = float(my_list[2])
if a == 0:
    print("Impossivel calcular")
else:
    if (b ** 2 - 4 * a * c) < 0:
        print("Impossivel calcular")
    else:
        R1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / ( 2 * a )
        R2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / ( 2 * a )
        print(f"R1 = {R1:.5f}")
        print(f"R2 = {R2:.5f}")
