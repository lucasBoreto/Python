from cadastro import *
from os import system
from time import sleep

while True:
	# manipulando os arquivos 
	try: # abre o arquivo
		arquivo = open('operacoes.txt', 'r+')
	except: # cria o arquivo 
		arquivo = open('operacoes.txt', 'x')
		arquivo = open('operacoes.txt', 'r+')
	lista_operacoes = [] 
	# lê conteudo de arquivo e armazena cada lista em lista_operacoes
	arquivo = arquivo.readlines() 
	for linha in arquivo:
		lista_operacoes.append(linha.split()) # adiciona listas em listas_operacoes ex: [['01/01/24', 'Salário', '1400', 'Receita'], ['02/01/24', 'Gorjeta', '20', 'Receita']]
	
	# menu do programa
	system('clear')
	print('-' * 45)
	print(f"{'Gestão Financeira':^45}")
	print('-' * 45)
	print('1 - Cadastrar operação\n2 - Exibir operacoes\n6 - Sair')
	opcao = int(input('Digite a opcao que deseja: '))
	match opcao:
		case 1: # cadastrar operacao
			operacao = Operacao()
			arquivo = open('operacoes.txt', 'w')
			# copia todas as listas em lista_operacoes para o arquivo
			for r in lista_operacoes:
				arquivo.write(f"{r[0]} {r[1]} {r[2]} {r[3]}\n") #ex: 01/01/24 Salário 1400 Receita
			arquivo.write(operacao.salvar_operacao()) # copia o novo cadastro com o formato {Data} {Nome_receita} {valor_receita}
			arquivo.close()       
		case 2: # exibir operacoes
			tipo_op = int(input('Digite o tipo de operação que deseja ver:\n1 - Receita  2 - Despesa'))
			system('clear')
			print('-' * 45)
			print(f"{'EXIBIR OPERAÇÕES':^45}")
			print('-' * 45)
			print(f"{'DATA':<12} {'NOME':^20} VALOR")
			if tipo_op == 1:
				for linha in lista_operacoes:
					if linha[3][0].upper() == 'R':
						print(f"{linha[0]:<12} {linha[1]:^20} R${linha[2]}")
			elif tipo_op == 2:
				for linha in lista_operacoes:
					if linha[3][0].upper() == 'D':
						print(f"{linha[0]:<12} {linha[1]:^20} R${linha[2]}")
		case 6: # sair do programa
			print('Obrigado por utilizar o programa!')			
			sleep(2)
			break
	print()
	continuar = input('--Digite qualquer coisa/Aperte Enter para continuar')
