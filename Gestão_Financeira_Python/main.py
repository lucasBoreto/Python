from cadastro import *
from os import system
from time import sleep

while True:
	# manipulando os arquivos 
	try: # abre o arquivo
		arquivo = open('receitas.txt', 'r+')
	except: # cria o arquivo 
		arquivo = open('receitas.txt', 'x')
		arquivo = open('receitas.txt', 'r+')
	lista_receitas = [] 
	# lê conteudo de arquivo e armazena cada lista em lista_receitas
	arquivo = arquivo.readlines() 
	for linha in arquivo:
		lista_receitas.append(linha.split())
	
	# menu do programa
	system('clear')
	print('-' * 45)
	print(f"{'Gestão Financeira':^45}")
	print('-' * 45)
	print('1 - Cadastrar receita\n2 - Exibir Receitas\n6 - Sair')
	opcao = int(input('Digite a opcao que deseja: '))
	match opcao:
		case 1: # cadastrar receita
			receita = Receita()
			arquivo = open('receitas.txt', 'w')
			# copia todas as listas em lista_receitas para o arquivo
			for r in lista_receitas:
				arquivo.write(f"{r[0]} {r[1]} {r[2]}\n") #ex: 01/01/24 Salário 1400
			arquivo.write(receita.salvar_receita()) # copia o novo cadastro com o formato {Data} {Nome_receita} {valor_receita}
			arquivo.close()       
		case 2:
			system('clear')
			print('-' * 45)
			print(f"{'EXIBIR RECEITAS':^45}")
			print('-' * 45)
			print(f"{'DATA':<12} {'NOME':^20} VALOR")
			for linha in lista_receitas:
				print(f"{linha[0]:<12} {linha[1]:^20} R${linha[2]}")
		case 6:
			print('Obrigado por utilizar o programa!')			
			sleep(2)
			break
	print()
	continuar = input('--Digite qualquer coisa/Aperte Enter para continuar')
