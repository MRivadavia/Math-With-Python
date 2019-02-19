

"""Programa que usa rótulos a números, define a números ou dados um nome, de modo geral, uma variável."""

a = 3  # é atribuído para a letra 'a' o valor 3 e reciprocamente é atribuído ao número 3 a letra 'a'.
b = 5  # é atribuído para a letra 'b' o valor 3 e reciprocamente é atribuído ao número 3 a letra 'b'.

print(a+1)  # o argumento recebe a adição 'a+1', e retornará 4.
print()

print(b + a)  # o argumento recebe a adição 'b+a', e retornará 8.
print()

print(a ** 2 + 7 * b + 1)  # o argumento recebe uma expressão  chamada quadrática por haver um expoente 2. Esta
# expressão, pela atribuição dada às variáveis 'a' e 'b' torna-se uma expressão numérica:  3**2+ 7*5+1.
# O resultado será 45.

c = 2 * a - 9  # Podemos atribuir a uma outra variável uma expressão que envolva outras variáveis já
# declaradas ou definidas anteriormente.  O resultado fica armazenado como número em 'c'. Podemos visualizar o
# resultado pela função PRINT.

print(c)  # imprime na tela o valor recebido por 'c'.

# Podemos atribuir a valores rótulos que são palavras ou combinação de palavras e números
# que, de modo geral, caracterizam um dado em específico.

# Calcular o índice de massa corporal
massa = 80  # massa de um corpo humano qualquer de 80 kilogramas.
altura = 1.75  # altura de um corpo humano qualquer de 1 metro e 75 centímetros.
indice = massa / altura ** 2  # indice é igual à divisão entre a massa em kilogramas pela altura ao quadrado em metros.
print(indice)
print()
# Suponhamos que queiramos calcular a média aritmética de quatro notas na disciplina de Python I.
# Introduziremos uma nova função para receber estes valores diretamente do teclado após a execução do programa.
# A função chama-se INPUT. Vejamos a sua funcionalidade:

nota1 = int(input('Digite a primeira nota:'))  # a função INPUT recebe como caracter o valor e a função
# INT converte para tipo INTEIRO armazena em nota1
nota2 = int(input('Digite a segunda nota:'))  # a função INPUT recebe como caracter o valor e a função
# INT converte para tipo INTEIRO armazena em nota2
nota3 = int(input('Digite a terceira nota:'))  # a função INPUT recebe como caracter o valor e a função
# INT converte para tipo INTEIRO armazena em nota3
nota4 = int(input('Digite a quarta nota:'))  # a função INPUT recebe como caracter o valor e a função
# INT converte para tipo INTEIRO armazena em nota4

MediaA = (nota1 + nota2 + nota3 + nota4) / 4

print('A média aritmética é:', MediaA)
print()
# Se desejarmos calcular com estas notas dadas a média geométrica e a média harmônica,
# termos as seguintes expressões, respectivamente:

MediaG = (nota1 * nota2 * nota3 * nota4) ** (1 / 4)  # A média geométrica é a raiz e-nésima do produto
# de e-nésimos fatores.
print('A média geométrica é:', MediaG)
print()

MediaH = 4 / ((1 / nota1) + (1 / nota2) + (1 / nota3) + (1 / nota4))  # A média harmônica é a divisão entre
# o número de # dados pela somatória dos inversos dos dados. Obs.: nenhum dado pode ser zero.
print('A média harmônica é:', MediaH)
print()

MediaHR = 4 / (1 / nota1 + 1 / nota2 + 1 / nota3 + 1 / nota4)# Observe que podemos excluir os parênteses que
# envolvem os quocientes na média harmônica, o resultado será equivalente ao anterior.

print('A média harmônica é:', MediaHR)
