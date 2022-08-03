teste = list()  # Cria uma nova lista vazia "Mundo 3 - Continuaçao"
teste.append('Gustavo')  # Adiciona a string 'Gustavo' ao final da lista "Mundo 3 - Continuaçao"
teste.append(40)  # Adiciona o número inteiro 40 ao final da lista "Mundo 3 - Continuaçao"

galera = list()  # Cria uma nova lista vazia "galera"
galera.append(teste)  # Adiciona a própria lista "Mundo 3 - Continuaçao" (e não uma cópia) à lista composta "galera"

print(teste)  # Exibe ['Gustavo', 40]
print(galera)  # Exibe [['Gustavo', 40]]

teste[0] = 'Maria'  # Muda o item [0] da lista "Mundo 3 - Continuaçao", de 'Gustavo' para 'Maria'
teste[1] = 22  # Muda o item [1] da lista "Mundo 3 - Continuaçao", de 40 para 22

print(teste)  # Exibe ['Maria', 22]

galera.append(teste)  # Adiciona novamente a própria lista "Mundo 3 - Continuaçao" (já modificada) à lista composta "galera"
print(galera)  # Exibe [['Maria', 22], ['Maria', 22]] (e não [['Gustavo', 40], ['Maria', 22]])
