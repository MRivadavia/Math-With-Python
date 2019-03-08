""""Programa que trabalha com funções II """

from fractions import Fraction

a = Fraction()  # Por definição, o numerador é zero e o denominador é 1. A variável 'a' recebe a fração 0/1.
print(a)  # Portanto, retorna zero.

b = Fraction(3 / 4)  # A função Fraction recebe em seu argumento uma fração e retorna a mesma fração.
print(b)  # A saída será 3/4.

c= Fraction('1.2')  # Se a função Fraction receber em seu argumento um número racional, a variável 'c' receberá
# um tipo de dado fractions.Fraction, ou seja, uma fração.
print(c)  # A saída impressa na tela será 6/5.

d = Fraction(1.1)  # Quando se insere no argumento de Fraction um número decimal não entre aspas, o python
# retornará uma fração aproximada ao valor decimal 1.1.
print(d)
e = Fraction(1.1).limit_denominator()  # Quando se insere no argumento de Fraction um número decimal não entre
# aspas, e utiliza o método limit_denominator() para converter em fração irredutível.
print(e)

# Exemplo: Seja um círculo de raio 12 cm e uma circunferência de 