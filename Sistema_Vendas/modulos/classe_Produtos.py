class Produto:
    """Classe dos Produtos
    - Cada produto possui seu codigo, nome, preços, quantidade, tipo e marca, caso tenha"""
    def  __init__(self, codigo, nome='ITEM', preco_credito=0, preco_debito=0, preco_pix=0, quantidade=0, tipo='', marca=''):
        self.codigo = codigo
        self.nome = nome.upper()
        self.marca = marca.upper()
        self.tipo = tipo.upper()
        self.preco_credito, self.preco_debito, self.preco_pix = preco_credito, preco_debito, preco_pix
        self.quantidade = quantidade

    def listar_info(self):
        """- Função para listar informações do produto de forma formatada"""
        print('-'*70)
        print(f"{'COD':^10}{'NOME':^10}{'MARCA':^10}{'TIPO':^10}{'PREÇOS':^10}{'QUANTIDADE':^10}")
        print(f'{self.codigo:^10}{self.nome:^10}{self.marca:^10}{self.tipo:^10}{self.preco_credito:^3}{self.preco_debito:^3}{self.preco_pix:^3}{self.quantidade:^10}')
        print('-'*70)

