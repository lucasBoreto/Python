from cadastro import *
from menu import *

# manipulando os arquivos
while True: 
	try: # abre o arquivo
		arquivo = open('operacoes.txt', 'r+')
	except: # cria o arquivo 
		arquivo = open('operacoes.txt', 'x')
		arquivo = open('operacoes.txt', 'r+')

	# lê conteudo de arquivo e adiciona listas em listas_operacoes ex: [['01/01/24', 'Salário', '1400', 'Receita'], ['02/01/24', 'Gorjeta', '20', 'Receita']]
	lista_operacoes = [] 
	arquivo = arquivo.readlines() 
	for linha in arquivo:
		lista_operacoes.append(linha.split()) 

	# menu principal do programa
	menu_programa = Menu('GESTÃO FINANCEIRA')
	menu_programa.titulo()
	opcao = menu_programa.opcoes('Cadastrar operação', 'Exibir operações', 'Remover operações', 'Sair')

	while True:
		match opcao:
			 # cadastrar operacao
			case 1:
				operacao = Operacao()
				arquivo = open('operacoes.txt', 'w')
				# copia todas as listas em lista_operacoes para o arquivo
				for r in lista_operacoes:
					arquivo.write(f"{r[0]} {r[1]} {r[2]} {r[3]}\n") #ex: 01/01/24 Salário 1400 Receita
				arquivo.write(operacao.salvar_operacao()) # copia o novo cadastro com o formato {Data} {Nome_receita} {valor_receita} {tipo_operacao}
				arquivo.close()       
				break
			
			# exibir operacoes
			case 2: 
				exibir_op = Menu('EXIBIR OPERAÇÕES')
				escolha_tipo_op = exibir_op.opcoes('Receita', 'Despesa')
				exibir_op.titulo()
				if escolha_tipo_op == 1:
					print(f"{'--RECEITA--':^45}\n")
					tipo_op = 'R'
				elif escolha_tipo_op == 2:
					print(f"{'--DESPESA--':^45}\n")
					tipo_op = 'D'
				
				# Mostrando a lista de operações de acordo com o tipo de operação (Receita ou Despesa)
				print(f"{'DATA':<18} {'NOME':<14} VALOR")
				for linha in lista_operacoes:
					if linha[3][0].upper() == tipo_op:
						print(f"{linha[0]:<12} {linha[1]:^20} R${linha[2]}")
				break
			
			# Remover operação
			case 3: 
				remover_op = Menu('REMOVER OPERAÇÔES')
				remover_op.titulo()
				# Mostrando a lista de operações
				print(f"{'N°':<3} {'DATA':<18} {'NOME':<14} VALOR")
				for n,linha in enumerate(lista_operacoes):
					print(f"{n} - {linha[0]:<12} {linha[1]:^20} R${linha[2]}")
				try:
					remover = int(input('Digite o numero da operação a ser removida[Espaço para cancelar]: '))
					del lista_operacoes[remover]
					print('Operação removida com sucesso!')
				except:
					print('Nenhuma operação removida!')
				# reescrevendo a lista de operações  
				arquivo = open('operacoes.txt', 'w')
				for r in lista_operacoes:
					arquivo.write(f"{r[0]} {r[1]} {r[2]} {r[3]}\n")
				arquivo.close()
				break

			# sair do programa
			case 4: 
				print('Obrigado por utilizar o programa!')			
				exit()

			case _:
				print('Nenhuma operação solicitada!')
				break
	continuar = input('--Digite qualquer coisa e/ou Aperte Enter para continuar ')
