class Operacao:

    def __init__(self): 
        # operacao pode ser receita ou despesa
        tipo_op = int(input('Qual tipo de operação deseja fazer?\n1 - Receita  2 - Despesa'))
        if tipo_op == 1:
            self.operacao = 'Receita'
        elif tipo_op == 2:
            self.operacao = 'Despesa'
        
        #informações da operação 
        nome_operacao = input(f'Digite o titulo da {self.operacao}: ')
        if nome_operacao == '':
            nome_operacao = self.operacao
        while True:
            try:
                valor_operacao = float(input(f'Digite o valor da {self.operacao}: '))
                data_operacao = input(f'informe a data da {self.operacao} com o formato (DD/MM/AA): ')
                self.nome_operacao = nome_operacao
                self.valor_operacao = valor_operacao
                self.data_operacao = data_operacao
                break
            except:
                print('Por favor, informe corretamente')
                

    def salvar_operacao(self):
        """- Retorna as informações do objeto para que sejam salvas em um arquivo txt"""
        return f"{self.data_operacao} {self.nome_operacao} {self.valor_operacao} {self.operacao}\n"
