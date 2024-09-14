def continuar():
    """
    - Função para continuar ou não em um trecho de código com while True
    retorno1 : caso resposta positiva, retorna True, continuando o loop
    retorno2: caso resposta negativa, retorna False, quebrando o loop
    """
    continuar = str(input('Deseja continuar?[Digite S para continuar]: '))[0].upper()
    if continuar in 'S':
        return True
    else:
        return False


def limparTela(tempo):
    """
    - Função para facilitar a visualização do usuario 
    parametro: tempo desejado que o terminal permaneça antes de ser apagado
    """
    from time import sleep
    from os import system
    sleep(tempo)
    system('clear')