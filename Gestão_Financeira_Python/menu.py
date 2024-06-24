from os import system

class Menu:
    def __init__(self, texto_titulo):
        self.texto_titulo = texto_titulo

    def titulo(self):
        system('clear')
        print('-' * 45)
        print(f"{self.texto_titulo:^45}")
        print('-' * 45)
    

    def opcoes(self, *opcao):
        for num, op in enumerate(opcao):
            print(f"{num + 1} - {op}")
        print()
        escolha = int(input('Digite a opcao que deseja: '))
        return escolha
