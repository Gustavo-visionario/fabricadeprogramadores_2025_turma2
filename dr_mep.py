def atendimento():
    valor_total = 0
    raças = ['pug', 'pastor-alemão', 'labrador']
    print(raças[0])
    print(raças[1])
    print('labrador' in raças)
    raças = ['pug', 'pastor-alemão', 'labrador']
    raça = input('insira uma raça: ')
    if (raça in raças):
        if (raça =='pug'):
            valor_total = valor_total + 70.99
            print(valor_total)
        elif (raça == 'pastor-alemão'):
            valor_total = valor_total + 120.99
            print(valor_total)
        elif (raça == 'labrador'):
            valor_total = valor_total + 110.99
            print(valor_total)
    else:
        print('atendimento indisponivel')
atendimento()       