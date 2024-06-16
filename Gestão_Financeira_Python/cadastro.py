class Receita:

    def __init__(self):
        nome_receita = input('Digite o titulo da Receita: ')
        while True:
            try:
                valor_receita = float(input('Digite o valor da Receita: '))
                data_receita = input('informe a data da operação com o formato (DD/MM/AA): ')
                self.nome_receita = nome_receita
                self.valor_receita = valor_receita
                self.data_receita = data_receita
                break
            except:
                print('Por favor, informe corretamente')
                

    def salvar_receita(self):
        """- Retorna as informações do objeto para que sejam salvas em um arquivo txt"""
        return f"{self.data_receita} {self.nome_receita} {self.valor_receita}\n"
    
