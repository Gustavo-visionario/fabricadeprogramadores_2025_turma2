estoque = { "Honda CG 160": [39.020, 10.00], 
            "Honda Biz": [22.613, 10.000],
            "Honda Pop 110i": [19.841, 12.000],
            "Honda NXR160 Bros":[16.225, 15.00],
            "Mottu Sport 110i": [10.241, 10.000], 
            "Honda CB 300F Twister": [5.877, 16.000],
            "Yamaha YBR 150 Factor": [5.517, 20.000],
            "Honda PCX 160": [4.730, 16.000], 
            "Honda XRE 300 Sahara": [4.013, 22.000],
            "Shineray JET125SS": [3.781, 14.000],
            "Yamaha Fazer 250": [3.604, 13.000],
            "Yamaha XTZ 250 Lander": [3.445, 10.000],
            "Yamaha Fazer 150": [3.425, 10.000],
            "Honda XRE 190": [3.180, 22.000],
            "Honda Elite 125": [2.989, 10.000],
            "Shineray SHI 175": [2.609, 12.000],
            "Yamaha Crosser 150": [2.510, 18.000],
            "Yamaha NMAX": [2.319,  10.000],
            "Shineray JET 50": [1.724, 8.000],
            "Shineray JEF 150": [1.677, 12.000], }

produto = input("digite o produto selecionado: ")
quantidade = int(input("digite a qauntidade: "))
venda = [ [produto, quantidade] ]
total = 0
if produto in estoque:
    print("vendas:\n")
    for operacao in venda:
        produto, quantidade = operacao
        preço = estoque[produto][1]
        custo = preço * quantidade
        print("%12s: %3d x %6.2f = %6.2f" %
              (produto, quantidade, preço, custo))
        estoque[produto][0]-= quantidade
        total += custo
else:
    print("nao temos este produto no estoque!")
print("custo total: %21.2f\n"% total)
print("estoque:\n")
for chave, dados in estoque.items():
    print("descricao: ",chave)
    print("quantidade: ", dados[0])
    print("preço: %6.0\n" % dados[1])