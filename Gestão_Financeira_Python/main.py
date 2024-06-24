from cadastro import *
from menu import *
from time import sleep

while True:
	# manipulando os arquivos 
	try: # abre o arquivo
		arquivo = open('operacoes.txt', 'r+')
	except: # cria o arquivo 
		arquivo = open('operacoes.txt', 'x')
		arquivo = open('operacoes.txt', 'r+')
	lista_operacoes = [] 
	# lê conteudo de arquivo e adiciona listas em listas_operacoes ex: [['01/01/24', 'Salário', '1400', 'Receita'], ['02/01/24', 'Gorjeta', '20', 'Receita']]
	arquivo = arquivo.readlines() 
	for linha in arquivo:
		lista_operacoes.append(linha.split()) 

	# menu do programa
	menu_programa = Menu('GESTÃO FINANCEIRA')
	menu_programa.titulo()
	opcao = menu_programa.opcoes('Cadastrar operação', 'Exibir operações', 'Remover operações', 'Sair')
	while True:
		match opcao:
			case 1: # cadastrar operacao
				operacao = Operacao()
				arquivo = open('operacoes.txt', 'w')
				# copia todas as listas em lista_operacoes para o arquivo
				for r in lista_operacoes:
					arquivo.write(f"{r[0]} {r[1]} {r[2]} {r[3]}\n") #ex: 01/01/24 Salário 1400 Receita
				arquivo.write(operacao.salvar_operacao()) # copia o novo cadastro com o formato {Data} {Nome_receita} {valor_receita} {tipo_operacao}
				arquivo.close()       
				break
		
			case 2: # exibir operacoes
				exibir_op = Menu('EXIBIR OPERAÇÕES')
				tipo_op = exibir_op.opcoes('Receita', 'Despesa')
				exibir_op.titulo()
				if tipo_op == 1:
					tipo_op = 'R'
					print('--RECEITAS')
				elif tipo_op == 2:
					tipo_op = 'D'
					print('--DESPESAS')
				print(f"{'DATA':<12} {'NOME':^20} VALOR")
				for linha in lista_operacoes:
					if linha[3][0].upper() == tipo_op:
						print(f"{linha[0]:<12} {linha[1]:^20} R${linha[2]}")
				break

			case 3: # Remover operação
				remover_op = Menu('REMOVER OPERAÇÔES')
				tipo_op = remover_op.opcoes('Receita', 'Despesa')
				remover_op.titulo()
				if tipo_op == 1:
					tipo_op = 'R'
					print('--RECEITAS')
				elif tipo_op == 2:
					tipo_op = 'D'
					print('--DESPESAS')
				for n,linha in enumerate(lista_operacoes):
					if linha[3][0].upper() == tipo_op:
						print(f"{n} - {linha[0]:<12} {linha[1]:^20} R${linha[2]}")
				remover = int(input('Digite o numero da operação a ser removida: ')) 
				del lista_operacoes[remover]
				arquivo = open('operacoes.txt', 'w')
				for r in lista_operacoes:
					arquivo.write(f"{r[0]} {r[1]} {r[2]} {r[3]}\n")
				arquivo.close()
				break

			case 4: # sair do programa
				print('Obrigado por utilizar o programa!')			
				sleep(2)
				exit()
			case _:
				print('Por favor, Digite uma operação válida!')
	print()
	continuar = input('--Digite qualquer coisa/Aperte Enter para continuar')
