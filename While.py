x = 10
while x <=0:
   print(x)
   print('FOGO!')
   x = x - 1


fim = int(input("digite o ultimo numero a imprimir"))
x = 0
while x <= fim:
   if x % 12 == 0:
      print(x)
   x = x + 1   

   fim = 9
   x = 0
   while x <= fim:
      if x % 2 == 0:
         print()
      else:
         print(x)
      x = x + 1

def arvore_de_natal():
      linha = 1
      while coluna <= linha:
         coluna = 1 
         print('💜',end="")
         coluna = coluna + 1
      print()
      linha = linha + 1
arvore_de_natal()                  