import math
my_list1 = input().split()
my_list2 = input().split()
x1, y1 = float(my_list1[0]), float(my_list1[1])
x2, y2 = float(my_list2[0]), float(my_list2[1])
distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(f'{distance:.4f}')
