my_list = input().split(' ')
A, B, C = float(my_list[0]), float(my_list[1]), float(my_list[2])
TRIANGULO = (1 / 2) * A * C
CIRCULO = 3.14159 * (C ** 2)
TRAPEZIO = (1 / 2) * (A + B) * C
QUADRADO = B ** 2
RETANGULO = A * B
print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')
