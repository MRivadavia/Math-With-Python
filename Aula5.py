

# Obtendo  entradas com INPUT e Tipos de Dados

# Vamos retomar um pouco mais esta função que nos será útil para toda aplicacão em Python.

# A função Input obtem uma string através da entrada de informações via teclado.

# Exemplo:

a = input()  # A variável 'a' está a receber qualquer informação via teclado. Se digitares World
print(a)  # a variável 'a' receberá esta string  e, então, printará na tela: World.

b = input()  # Se digitares o número 7, a função Input armazenará na variável 'b' o número sete como uma String.
print(type(b))  # Observe que a variável 'b' recebeu um tipo de dados String.

# Agora, se quisermos manipular estes tipos de dados numericamente, é necessário introduzirmos a função Int.
# que converte String em tipo de dados numérico Inteiro.

c = int(a) + int(b)  # Se entrares para 'a' um valor numérico e para 'b' o mesmo, então pela função Int estes valores
# converterão em tipo de dados Inteiro que será armazenado em 'c'.
print(c)  # Veja o tipo de saída abaixo com a função Type.
print(type(c))
print()

a=input('Entre com um valor inteiro:')  # O programa pede para que o valor de entrada seja um número inteiro.
# Lembre que a função Input retorna como saída para a variável 'a' uma string e não um tipo numérico inteiro.
print('A soma de', a, 'mais',a , 'é igual a: ',a+a)  # Assim, na tela aparecerá como resultado uma concatenção
# da variável 'a' consigo mesma, pois foi inserida como argumento da função Print um sinal de + que compreende
#como concatenação .

a=input('Entre com um valor inteiro:')
print('A soma de', a, 'mais',a , 'é igual a: ',int(a)+int(a))

# Podemos converter as strings em tipo de dados de ponto flutuante.
a=input('Digite um valor:')  # A função Input aceita em seu argumento uma mensagem de interação com o usuário.
b=input('Digite outro valor:')
c=float(a)+float(b)  # As variáveis 'a' e 'b' receberam da função Input os valores numéricos como String e pela
# função Float os converterá para tipo de dados ponto flutuante.
print(c)  # O resultado é apresentado na tela.
print(type(c))  # É mostrado pela função Type o tipo de dado armazenado em 'c'.
print()

""""Parte do código a seguir há erro proposital."""
# Parte 1
a = input('Entre com um valor decimal:')  # A intenção é mostrar que entrando com um valor decimal haverá
# problemas ao tentar somar sem fazer uso de conversão de formato de String para quelquer tipo numérico.
print(type(a))  # É printado na tela que o tipo de dados recebido pela variável 'a' é uma String.
b = a + 5  # A variável 'a', tipo String, quando adicionada ao número 5 retornará um aviso de erro de
# rastreamento, ou seja, um Traceback.
print()
b = float(a) + 5  # A variável 'a' contendo um tipo de dados String entra como argumento  na função Float
# e converte para ponto flutuante, ou seja, decimal.
print(b)  # Mostra na tela a soma acima.
print()
# Fim Parte 1

""""Parte 2 de código com erro proposital."""
# Parte 2
a = input('Entre com um valor decimal:')  # Entrando com um valor decimal, a variável 'a' recebe como tipo de
# dados String.
print(type(a))  # A função Type, através da função Print, mostra o tipo de dado String para a variável 'a'.
print()
b = int(a) + 5  # A função Int não será capaz de converter o tipo String para Inteiro.
b= int(float(a)) +5  # A função Int  converte para inteiro a variável 'a' que foi alterada para o
# tipo de dados ponto flutuante e adiciona ao 5 resultando em 7.
print(b)  # É mostrado na tela a soma.
print()
# Fim Parte 2

a=float(input('Entre com um valor fracionário:'))
print(a)  # Note que o python mostrará um erro que não foi possível converter um valor fracionário em
# tipo flutuante.

try:
    a=float(input('Entre com um valor fracionário:'))
except ValueError:
    print('Erro!')