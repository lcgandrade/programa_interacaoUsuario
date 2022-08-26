'''
Gerar um programa que calcula a média de N valores recebidos via teclado,
e ao final mostra a soma dos valores, a quantidade de valores digitados
e o valor da média calculada
'''

def gerador():
    soma= 0
    qtd= 0
    while(True):
        entrada = float(input('Entre com um número: '))
        if(entrada == 0):
            break
        soma+=entrada   #acumulador
        qtd+= 1         #contador
    media= soma/qtd
    print('Soma: ', soma)
    print('Quantidade: ', qtd)
    print('Média: ', media)

def programa():
    while True:
        try:
            gerador()
            break
        except ValueError:
            print('O valor registrado necessita ser do tipo número e não pode haver vírgulas (utilize "." para separador decimal)\n')

def welcome():
    print('Bem vindo ao programa teste_one ' + "\U0001F603 \n") # Unicodes de emoji comuns com seus nomes abreviados CLDR
    print('O objetivo é receber valores registrados pelo usuário, efetuar a soma, contagem e média dos valores retornando uma análise descritiva de dados \n')
    print('Instrução: Digite os valores desejados e para concluir digite 0')
    print('Regras: Digite somente números e utilize "." para separador decimal \n')
    while True:
        condicao= str(input('Vamos iniciar? SIM ou NÃO?')).upper()
        if condicao == "NÃO":
            print("\U0001F622" + ' Ah, que pena.. Até a próxima ' + "\U0001F609")
            break
        elif condicao == "SIM":
            programa()
        else:
            print("\U0001F62F " + ' Desculpe essa opção não existe. Responda "SIM" ou "NÃO"')

welcome()







