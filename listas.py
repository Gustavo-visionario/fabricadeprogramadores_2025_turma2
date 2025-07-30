import math
def equacao():
    a = float(input("insira o valor de A: "))
    b = float(input("insira o valor de B: "))
    c = float(input("insira o valor de C: "))
    delta = b**2 - 4 * a * c
    if delta >= 0:
        #calculo da raiz real
       x = (-b + math.sqrt(delta)) / 2*a
       y = (-b - math.sqrt(delta)) / 2*a 
       print("o resultado e " , x,y)
    else:
        print('''essa equação não possui
              raizes reais''')
#equacao()
import random

numero_aleatorio = random.randint(0,10)
print(numero_aleatorio)

frutas_aleatorias = ["uva,'morango','abacaxi','abacate','limao','acerola','laranja','mexerica','mamao','tomate"]
print(random.choice(frutas_aleatorias))

