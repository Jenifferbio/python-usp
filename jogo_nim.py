tipo_jogo = 0

def computador_escolhe_jogada(n,m):
    print('Computador começa!')
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        return m

def usuario_escolhe_jogada(n,m):
    print('sua vez!\n')
    jogada = 0
    while jogada == 0:
        jogada = int(input('Quantas peças irá tirar?'))
        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0
    return jogada

def partida():
    print('')

    n = int(input('quantas peças?'))
    m = int(input('limite de peças por jogada?'))
    computador_ganha = True
    if n % (m+1) == 0:
        print('Você começa!')
        computador_ganha = False

    while n > 0:
        if computador_ganha:
            jogada = computador_escolhe_jogada(n,m)
            computador_ganha = False
            print('Computador retirou {} peças'.format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n,m)
            computador_ganha = True
            print('Você retirou {} peças'.format(jogada))
        n = n - jogada
        print('Restam apenas {} peças em jogo.\n'.format(n))

    if computador_ganha:
        print('Você ganhou!')
        return 1
    else:
        print('Computador ganhou!')
        return 0

def campeonato():
    usuario = 0
    computador = 0

    for i in range(3):
        vencedor = partida()

        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    print('Placar final: você {} x {} computador'.format(usuario, computador))

while tipo_jogo == 0:
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')

    tipo_jogo = int(input('Sua opção:'))
    print('')

    if tipo_jogo == 1:
        print('Você escolheu partida isolada!')
        partida()
        pass
    elif tipo_jogo == 2:
        print('Você escolheu um campeonato!')
        campeonato()
        pass
    else:
        print('Opção inválida!')
        tipo_jogo = 0


