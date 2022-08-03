# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.]
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Partidas {jogador["nome"]} joogou: '))
    partidas.clear()
    for c in range (0,tot):
        partidas.append(int(input(f'Quantos gols na partida{c+1}:')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar: [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responsa S ou N')
    if resp == 'N':
           break
print('_'*30)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('_'*30)

for k, v in enumerate(time):
    print(f'{k:>4}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
while True:
    busca = int(input('Mostrar os dados de qual jogador : [999 para Parar]'))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Eerro! Nao existe jogador com o codigo {busca}')
    else:
        print(f'Levantando os dados do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
