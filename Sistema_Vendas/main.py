from modulos.classe_Produtos import *
import os

while True:

    #bloco repetido
    os.system('cls')
    print('-'*70)
    print(f"{'BEM VINDO AO SISTEMA DE VENDAS!':^70}")
    print('-'*70)
    
    print('Digite a opção que deseja e tecle enter:\n1 - Cadastrar produto\n2 - Sair')
    opcao = int(input(':'))
    match opcao:
        case 1:

            #bloco repetido
            os.system('cls')
            print('-'*70)
            print(f"{'DIGITE A INFORMAÇÃO E TECLE ENTER':^70}")
            print('-'*70)
            
            nome = str(input('Digite o nome do produto: ').upper())
            preco_credito = float(input('Digite o preco de CRÉDITO do produto em R$:').replace(',', '.'))
            preco_debito = float(input('Digite o preco de DÉBITO do produto em R$:').replace(',', '.'))
            preco_pix = float(input('Digite o preco de PIX do produto em R$:').replace(',', '.'))
            quantidade = int(input('Digite a quantidade do produto:'))
            tipo = str(input('Digite o tipo do produto[exemplo: Fruta, Ferramenta, iluminação]:').upper())
            marca = str(input('Digite a marca do produto, caso haja: ').upper())
            novo_Produto = Produto(1, nome, preco_credito, preco_debito, preco_pix, quantidade, tipo, marca)

            novo_Produto.listar_info()
            
        case 2:
            os.system('cls')
            print('Obrigado por utilizar o sistema!')
            exit()
        
#novo_produto = Produtos(1, 'Banana', 10, 5, 3, 1, 'Fruta') #Criação do produto BANANA
#print(novo_produto.precos)
#novo_produto.listar_info()
