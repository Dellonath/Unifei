'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:

'''
# importanto os para clear
import os 

# criando o painel

def painel():
    print('VOTAÇÃO DE MELHOR OS')
    print('1 - Windows\n2 - Unix\n3 - Linux\n4 - Netware\n5 - MacOS\n6 - Outro\n0 - Sair')

# criando o sistema para clear()
clear = lambda: os.system('clear')

# criando a lista de valores
lista = []

# loop infinito e votação
while True:
    clear()
    painel()
    print('Digite um dos valores acima: ', end='')
    escolha = int(input())
    if escolha == 1:
        lista.append(1)
    elif escolha == 2:
        lista.append(2)
    elif escolha == 3:
        lista.append(3)
    elif escolha == 4:
        lista.append(4)
    elif escolha == 5:
        lista.append(5)
    elif escolha == 6:
        lista.append(6)
    elif escolha == 0:
        break
    else:
        print('Não é possível outros valores além dos listados. Presione ENTER.', end = '')
        input()

# fornecendo os resultados
print(f'\nRESULTADO Total de votos {len(lista)}.\n ')

# definindo o vencedor
i = 1
vencedor = []
while i <=6:
	vencedor.append(lista.count(i))
	i += 1
i = vencedor.index(max(vencedor)) + 1
# fornecendo o resultado
if i == 1:
    print(f'O Sistema Operacional mais votado foi o Windows, com {lista.count(1)} votos, correspondendo a {int(lista.count(1)*100/len(lista))}% dos votos.')
elif i == 2:
    print(f'O Sistema Operacional mais votado foi o Unix, com {lista.count(2)} votos, correspondendo a {int(lista.count(2)*100/len(lista))}% dos votos.')
elif i == 3:
    print(f'O Sistema Operacional mais votado foi o Linux, com {lista.count(3)} votos, correspondendo a {int(lista.count(3)*100/len(lista))}% dos votos.')
elif i == 4:
    print(f'O Sistema Operacional mais votado foi o Netware com {lista.count(4)} votos, correspondendo a {int(lista.count(4)*100/len(lista))}% dos votos.')
elif i == 5:
    print(f'O Sistema Operacional mais votado foi o MacOS, com {lista.count(5)} votos, correspondendo a {int(lista.count(5)*100/len(lista))}% dos votos.')
else:
    print(f'O Sistema Operacional mais votado foi o Outros, com {lista.count(6)} votos, correspondendo a {int(lista.count(6)*100/len(lista))}% dos votos.')

