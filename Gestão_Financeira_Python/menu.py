from os import system

class Menu:
    def __init__(self, texto_titulo):
        self.texto_titulo = texto_titulo

    def titulo(self):
        """-> Mostra um cabeçalho com o titulo do menu """
        system('clear')
        print('-' * 45)
        print(f"{self.texto_titulo:^45}")
        print('-' * 45)
    

    def opcoes(self, *opcao):
        """-> Mostra as opções disponiveis para escolher
        param opcao: Recebe uma tupla com as opções para se escolher
        return escolha: retorna o numero da opção escolhida pelo usuario """
        for num, op in enumerate(opcao):
            print(f"{num + 1} - {op}")
        print()
        while True:
            try:
                escolha = int(input('Digite a opcao que deseja[Espaço para sair]: '))
                if 0 <= escolha <= len(opcao):
                    return escolha       
                print('Digita algo válido!')                
            except:
                break