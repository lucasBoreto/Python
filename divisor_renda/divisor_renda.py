# imports
import utilidade

# inputs
lista_rendas = []
dict_despesas = {}
continuar = True
while continuar:
    utilidade.limparTela(1)
    try:
        nome_renda = str(input('Digite o nome da renda: '))
        valor_renda = float(input(f'Digite o valor recebido de {nome_renda}: R$'))
        utilidade.limparTela(1)
        lista_rendas.append(nome_renda)
        lista_rendas.append(valor_renda)
        continuar = utilidade.continuar()
    except: 
        print('Você digitou um valor errado, por favor, digite um valor correto')

continuar = True
porcentagem_uso = 100
while continuar:
    utilidade.limparTela(2)
    print(f'Você tem {porcentagem_uso}% da renda disponivel')
    try:
        nome_despesa = str(input('Digite o nome da despesa: '))
        porc_despesa = float(input(f'Digite a pocentagem separada para {nome_despesa}: '))
        if porcentagem_uso <= 0:
            print(f'Você não tem mais renda para alocar')
            break
        elif porc_despesa > porcentagem_uso:
            print(f'Você tem apenas {porcentagem_uso}% para usar, por favor, use o que está no seu orçamento!')
        else:
            porcentagem_uso -= porc_despesa
        utilidade.limparTela(1)
        dict_despesas[f'{nome_despesa}'] = porc_despesa
        continuar = utilidade.continuar()
    except: 
        print('Você digitou um valor errado, por favor, digite um valor correto')
        
# processamento
utilidade.limparTela(2)
tot_renda = 0
for valor in range(0, len(lista_rendas), 2):
    tot_renda += lista_rendas[valor + 1]

# output
for nome, porcentagem in dict_despesas.items():
    valor_despesa = porcentagem / 100 * tot_renda
    print(f'{nome:} : R${valor_despesa} ({porcentagem}%)')
