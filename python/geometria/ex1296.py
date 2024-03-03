# Cálculo da área de um triângulo a partir de suas medianas
# Cada caso de teste é composto por três números que denotam o comprimento das medianas do triângulo

import math

while True:
    try:
        m1, m2, m3 = map(float, input().split())
        sm = (m1+m2+m3) / 2
        area = 4/3 * math.sqrt(sm * (sm-m1) * (sm-m2) * (sm-m3))
        if area <= 0: area = -1.000
    except EOFError:
        break
    except ValueError:
        area = -1.000
    
    print(f'{area:.3f}')