""""Determina se um número inteiro é fator de outro"""


# Programa que determina se um número inteiro é fator de outro sem o uso de laço For, afim de executar uma única vez o
# programa.


def is_fatores(a, b):  # É criada uma função que recebe dois números e é determinado se um número é fator de outro.
    if a % b == 0:  # Se o resto da divisão entre a e b, ou seja, a divisão de a por b for igual a zero, então:
       print('O número ', b, 'é um fator de', a)  # será impressa a mensagem que o número é fator de outro.
    else:  # senão, se a divisão de a por b for diferente de zero, entao:
        print('O número ', b, 'não é um fator', a)  # será impressa a mensagem que o número não é fator de outro.


a = int(input('Entre com um número inteiro qualquer:'))
b = int(input('Entre com um número inteiro qualquer diferente de zero:'))
is_fatores(a, b)

##############################################

# Programa que determina se um número inteiro é fator de outro com o uso de laço For, afim de executar até decidir a
# saída do programa.

for k in range(1,100):
    a = int(input('Entre com um número inteiro qualquer:'))
    b = int(input('Entre com um número inteiro qualquer diferente de zero:'))
    is_fatores(a, b)  # É chamada a função definida como is_fatores cujos argumentos recebem dois números inteiros.

    print('Deseja sair(y/n)?')  # Pergunta ao usuário deseja sair do programa digitando 'y', para continuar outra tecla
    char = input()  # A variável 'char' recebe um String 'y' para ser testada na instrução If a seguir.
    if char == 'y':  # Se 'char' recebeu pela função Input 'y', então será executada a
        break  # função Break que interromperá o programa.
    else:  # Senão  irá executar a próxima instrução dada pela função Pass que deixa "passar", ou seja, dá continuidade
        pass  # ao programa.





