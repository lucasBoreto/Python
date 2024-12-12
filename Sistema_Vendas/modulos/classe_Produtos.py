class Produtos:
    def  __init__(self, codigo, nome='ITEM', precos={'CRÉDITO':0, 'DÉBITO':0, 'DINHEIRO':0 }, quantidade=0, tipo='', marca=''):
        self.codigo = codigo
        self.nome = nome.upper()
        self.marca = marca.upper()
        self.tipo = tipo.upper()
        self.precos = [precos[0], precos[1], precos[2]]
        self.quantidade = quantidade

    def listar_info(self):
        print('-'*70)
        print(f"{'COD':^10}{'NOME':^10}{'MARCA':^10}{'TIPO':^10}{'PREÇOS':^10}{'QUANTIDADE':^10}")
        print(f'{self.codigo:^10}{self.nome:^10}{self.marca:^10}{self.tipo:^10}{self.precos[0]:^3}{self.precos[1]:^3}{self.precos[2]:^3}{self.quantidade:^10}')
        print('-'*70)

    def salvar_produto(self):
        produto = open()