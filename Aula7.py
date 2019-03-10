
""""Programa que fará uso dos laços de repetiçòes e desvios condicionais."""


# Desejamos nesta aula calcular se um número inteiro qualquer é fator de outro.
# Dizemos que um número 'a' é fator de outro número inteiro 'b' se 'a' divide 'b' deixa resto zero.
# Disto, podemos dizer que um número 'a' ser fator de outro número 'b' é equivalente a dizer que 'a' é divisor de 'b'.
# Quando há resto zero, dizemos que a divisão é exata.
# Um exemplo: O número 6 divide o número 42 e deixa resto zero.
# Vamos elaborar dois métodos para avaliar se um número é divisor de outro.

# Primeiro método, uso do laço FOR.

# O laço For é uma estrutura de repetição que gerencia a variável de loop(laço).

# Ex.1:

for x in range(0, 10):  # Nesta instrução, a variável 'x' tomará sucessivamente um valor de Range,
    # que neste caso está especificado  dentro de um intervalo de Zero a Nove. Deve-se considerar
    # o último valor do par ordenado de Range como sendo o valor declarado menos um.
    y = 2 * x  # O valor de 'x'que varia a cada laço é multiplicado por dois e armazenado na variável 'y'.
    print(y)  # É impresso na tela os valores de 'y'.

# Ex.2:

for x in range(0, 11):  # Nesta instrução, a variável 'x' variará de 0 a 10, como explicado anteriormente.
    y = 5 * x  # 'x' que varia dentro da faixa(Range) é multiplicado por 5 e armazenado o resultado na variável 'y'.
    print(y, end=' ')  # É impresso na tela os valore de 'y', contudo o argumento em Print, "end=' '", toma os
    # os valores de 'y' e os ordena horizontalmente, enquanto que na instrução do exemplo anterior ordena
    # verticalmente.
    print()

# Estrutura de desvio condicional.  Função IF, ELSE.
# Uma  declaração If se faz uso quando desejamos realizar comparações entre variáveis.
# Mais simplesmente como: Se(If) 'declaração', entáo uma ou mais instruções serão executadas.
# A condição Else é usada quando a condição If não for satisfeita. É realizado um desvio.
# Mais simplesmente como: Se(If) 'declaracao' não for satisfeita, a condição Else é testada, então uma ou
# mais instruções serão executadas.

x = int(input('Entre com um valor inteiro para x: '))  # Inserindo um valor inteiro para x
y = int(input('Entre com um valor inteiro para y: '))  # Inserindo um valor inteiro para y

if x == y:  # A declaração x igual y é testada pela condicional IF.
    print('O valor x =', x, 'é igual ao valor y =', y)  # É executada esta impressão caso  x for igual a y.
else:  # bloco de instrução à condição de desvio Else será executada quando x não for igual a y.
    print('O valor x =', x, 'é diferente do valor y =', y)  # É executada esta instrução caso a condição x não
for igual a y.

# Realizamos acima algumas explicações iniciais de como usar o Loop For e os Desvios If-Else.

# Vamos para o exemplo que desejamos tratar com respeito a um número ser fator de outro.

x = int(input('Entre com um número inteiro qualquer:'))  # Inserindo um valor inteiro para x
y = int(input('Entre com um número inteiro qualquer diferente de zero:'))   # Inserindo um valor inteiro para y

if x % y == 0:  # Se o resto da divisão entre x e y, ou seja, a divisão de x por y for igual a zero, então:
    print('O número ', y, 'é um fator de', x)  # esta instrução será executada.
else:  # Senão, ou seja, se o resto da divisão entre x e y for diferente de zero, entao:
    print('O número ', y, 'não é um fator', x)  # esta intrução será executada.

# Nesta aplicação acima, o programa será executado uma única vez, isto porque não estamos usando ainda uma
# estrutura de repetição, tal como o loop For. Insiramos esta estrutura para que possamos testar ad infinitum
# se um número é fator de outro.


for k in range(1,100):  # O valor K percorrerá valores de 1 a 99.
    x = int(input('Entre com um número inteiro qualquer:'))  # Inserindo um valor inteiro para x
    y = int(input('Entre com um número inteiro qualquer diferente de zero:'))  # Inserindo um valor inteiro para y

    if x % y == 0:  # Se o resto da divisão entre x e y, ou seja, a divisão de x por y for igual a zero, então:
        print('O número ', y, 'é um fator de', x)  # esta instrução será executada.
    else:  # Senão, ou seja, se o resto da divisão entre x e y for diferente de zero, entao:
        print('O número ', y, 'não é um fator', x)  # esta intrução será executada.

    print('Deseja sair(y/n)?')  # Pergunta ao usuário deseja sair do programa digitando 'y', para continuar outra tecla
    char = input()  # A variável 'char' recebe um String 'y' para ser testada na instrução If a seguir.
    if char == 'y':  # Se 'char' recebeu pela função Input 'y', então será executada a
        break  # função Break que interromperá o programa.
    else:  # Senão  irá executar a próxima instrução dada pela função Pass que deixa "passar", ou seja, dá continuidade
        pass  # ao programa.
