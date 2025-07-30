"""texto_escrito = "este livro e legal"
outro_texto = "vou aprender a programar"
texto=
#segunda linha
#terceira linha
print(texto)
#print("t\eu me chamo \"'Gustavo\"!!!")
outro_texto=texto_escrito 
pacotes_doritos = 5
quantidades = 7
pacotes_doritos -= quantidades
print(pacotes_doritos)

pacotes_doritos += quantidades
print(pacotes_doritos)

pacotes_doritos -= quantidades
print(pacotes_doritos)

pacotes_doritos *= quantidades
print(pacotes_doritos)

pacotes_doritos /= quantidades
print(pacotes_doritos)
carteira_digital = 0
print(carteira_digital)

carteira_digital += 100
print(carteira_digital)
carteira_digital -= 75.99
print(carteira_digital)
carteira_digital += 200
print(carteira_digital)
#funcoes.py 

SIGA SEUS SONHOS
EU TE AMO ANALY
""""""
def dizer_ola(nome_usuario = "gustavo"):
    print("ola",nome_usuario)
dizer_ola("analy")   
dizer_ola() 
dizer_ola("cachorro")
dizer_ola("244")
dizer_ola(8+8)

numero = 3
def apresentar_numero():
    #global numero 
    numero = 2
    print(numero)
apresentar_numero()
print(numero)

numero=5
def apresentar_numero2():
    global numero
    numero = 2
    
    numero=5
    print(numero)
apresentar_numero2()
"""
def quadrado(area):
    resultado = area* area
    return resultado
print(quadrado(5))

def conversor (celsius):
    fahrenheit = (9*celsius+160)/5
    return fahrenheit
print(conversor(100))

def salario(reajuste):
    reajuste += reajuste * 0.15
    return reajuste
print(salario(2000))

def volume(comp,alt,larg):
    return comp*alt*larg
print(volume(3,3,3))

def valores(x,y):
    z=x
    x=y
    y=z
    return ("o valor de x e: ",x,
            "e o valor de y e: ",y)
print(valores(20,3))

