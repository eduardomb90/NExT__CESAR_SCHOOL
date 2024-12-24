from personagem import Personagem
from inimigo import Inimigo

jogador = Personagem('Eduardo', 50, 10)
vilao = Inimigo('Orc', 30, 5)

print('Bem-vindo ao Jogo de Turnos!')

while True:


    if jogador.get_vida() > 0:
        print('--- Turno do Jogador ---')
        print('Escolha uma ação:')
        print('1. Atacar')
        print('2. Defender')
        print('3. Usar Habilidade Especial')
        opcao = input('Digite o número da sua ação: ')

        match opcao:
            case '1':
                dano = jogador.atacar()
                vilao.receber_dano(dano)
            case '2':
                jogador.defender()
            case '3':
                dano = jogador.usar_habilidade_especial()
                vilao.receber_dano(dano)


    if vilao.get_vida() > 0:
        print('--- Turno do Inimigo ---')
        acao_inimigo = vilao.agir()

        match acao_inimigo:
            case 1:
                dano = vilao.atacar()
                jogador.receber_dano(dano)
            case 2:
                vilao.defender()

    if jogador.get_vida() == 0:
        print(f'{jogador.get_nome()} foi derrotado!\n\n')
        print('--- Fim do Jogo ---')
        print(f'{jogador.get_nome()} perdeu!')
        break
    elif vilao.get_vida() == 0:
        print(f'{vilao.get_nome()} foi derrotado!\n\n')
        print('--- Fim do Jogo ---')
        print(f'{jogador.get_nome()} venceu!')
        break