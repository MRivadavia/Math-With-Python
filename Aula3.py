""""Programa que trabalha com frações I """

# Para usar frações em Python é necessário importarmos um módulo, o módulo FRACTIONS.
# Módulo, simplificadamente, é um programa que alguém escreveu pra ser usado em outro programa Python.
# O módulo Fractions nos fornece suporte para trabalharmos com números racionais.

from fractions import Fraction

f = Fraction(3, 4)  # a função Fraction recebe o primeiro argumento como numerador e no segundo como denominador.
# o rótulo f recebe o valor 3/4.
print(f)  # A função PRINT recebe em seu argumento o valor de f e imprime na tela a fração três quartos.
print()
print(Fraction(3, 4))  # Ao invés de usar no argumento a variável f, podemos usar uma função como argumento de outra
# função.
print(type(f))  # retorna o tipo numérico fractions.Fraction

# Podemos verificar a equivalência entre as frações, por exemplo.

a = Fraction(10, 18)

b = Fraction(15, 27)

print(a)
print()
print(b)
# Observe que tanto a variável 'a' como 'b' resultam em um mesma fração chamadas de equivalentes.
# Em outras palavras, duas frações são equivalentes se a diferença entre elas for igual a zero.
# Ex. Tomando como exemplo as frações definidas acima pelas variáveis 'a' e 'b'.
print(a-b) # se o resultado for zero, isto é, se 10/18 -15/27 = 0, então são equivalentes.
print()
# duas frações não são equivalentes se a diferença entre elas é diferente de zero.
# Ex. Vamos definir novas frações para as variáveis 'a' e 'b'.

a = Fraction(21, 12)

b = Fraction(3, 8)

print(a-b)  # a diferença resultou em um valor diferente de zero, isto é, não são equivalentes.

# Podemos Adicionar ou subtrair frações, por exemplo:

x = Fraction(1, 3)
y = Fraction(2, 5)
z = Fraction(3, 8)

R = x + y + z  # A variável R receberá o valor da soma das frações x, y e z.
print(R)  # Imprimindo na tela o resultado da soma das frações acima armazenada em R.
print()
R = 2 * x - 3 * y + 4 * z
print(R)  # Note que a fração x foi multiplicada por 2, a fração y por -3 e a fração z por 4.
print()

# Multiplicação e Divisão de frações.
# Tomemos os mesmos valores declarados a x, y e z acima.

R = x * y
print(R)  # imprime uma multiplicação entre as frações x e y.
print()

R = Fraction(x, y)  # observe que no próprio argumento da  função Fractions inserimos as frações x e y.
# em verdade, estamos realizado uma divisão entre duas frações x/y ou 1/3 dividido por 2/5.
print(R)
print()

R = Fraction(z, 3)  # É uma divisão da fração 3/8 pelo número 3.
print(R)
print()

R = Fraction(3, z)  # É uma divisão do número 3 pela  fração 3/8.
print(R)

# Podemos realizara Potenciação e Radiciação de frações.
# Sejam:

a = Fraction(2, 3)
b = Fraction(4, 3)
c = Fraction(1, 25)  # Então:

R = a ** 2
print(R)  # Imprime na tela 4/9
print()
R = b ** 3
print(R)  # Imprime na tela 64/27
R = c ** (Fraction(1, 2))  # Note que o expoente pode ser expresso na forma de fração para
# indicar uma radiciação.
print(R)  # Imprime na tela 0.2, que é equivalente a 1/5.  Veremos isto na próxima aula.
print()
# Aproveitaremos para exprimir uma expressão numérica racional.

R = a + 2*a ** 3 - b * a + 4 / c + 2
print(R)

frac = Fraction(Fraction(2, 5), Fraction(3, 8))
print(frac)
