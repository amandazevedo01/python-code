#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.]
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Partidas {jogador["nome"]} joogou: '))
for c in range (0,tot):
    partidas.append(int(input(f'Quantos gols na partida{c+1}:')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-'*30)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*30)
print(f'O jogador {jogador["nome"]} jogou{len(jogador["gols"])}')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')