""" Primeiro programa com matemática"""

"""Python é uma potente calculadora
    pode-se avaliar o valor de uma operação matemática
    ou de uma expressão matemática"""

"""Observação: todo resultado que deseja ser
    mostrado na tela deve estar entre os parenteses
    da função PRINT"""

# Hashtag insere comentário


#  ADIÇÃO:  SÍMBOLO:  +

print(1+2)  # a função PRINT recebe como argumento a adição 1+2 e retornará no terminal 3.
print()  # a função Print não recebe argumento, o python interpreta como linha em branco.
print(12+10+8+6+3+2+1)  # o argumento aqui é uma adição de várias parcelas cuja a soma retornará 42.

#SUBTRAÇÃO : SÍMBOLO;  -

print(8-3)  # a função PRINT recebe como argumento a subtração entre dois números e retornará 5.
print()
print(-7+(-3))  # a função PRINT recebe como argumento uma adição de dois números negativos e retorna -10.
print()
print(-19+7)  # a função recebe a adição de dois números inteiros e retorna no terminal -12.
print()
print(15-8-3)  # a função recebe subtrações e retorna 4

# MULTIPLICAÇÃO: SÍMBOLO: *

print(3*5)  # a função recebe uma multiplicação e retorna 15.
print()
print(5*2*7)  # função recebe três fatores e retorna 70.
print(type(2*3*4*5))  # A função Type nos revela que o tipo de saída da multiplicação entre inteiros é inteiro.

# Divisão: Símbolo: /

print(18/3)  # a função recebe a divisão de 18 por 3 e retorna 6.
print()
print(431/9)  # a função recebe a divisäo entre dois números inteiros e retorna um racional(ponto flutuante)
print(type(431/9))  # a função PRINT imprime na tela o tipo numérico com uma nova função TYPE.
print()
print(int(28/7))  # Se quisermos que o resultado entre dois números inteiros retorne inteiro é necessário
# usarmos a função INT e em seu argumento a divisão.
print(type(int(28/7)))  # Aqui mostra o tipo numérico de saída  que é inteiro.

# Resto de uma divisão: Símbolo %

print(9 % 4)  # a função PRINT imprime na tela o resto da divisão entre 9 e 4 que é 2.
print()
print(type(9 % 4))  # o resto da divisão tem como saída um número inteiro.

#  Menor inteiro em uma divisão. Símbolo: //

print(13 // 5)  # O resultado desta divisão é  2.6, mas o python retornará a parte inteira da divisão que é 2.
print()
print(-17 // 3)  # O resultado desta divisão é -5.666..., um valor negativo, mas o menor inteiro  imediatamente
# inferior a este  resultado  é -6, portanto o python retornará como o menor inteiro desta divisão o valor -6.

# POTENCIAÇÃO E RADICIAÇÃO.  SÍMBOLO: **

print(5**2)  # A função PRINT retorna a potência de cinco elevado ao quadrado que é 25.
print(type(5**2)) # A operação de potenciação retorna um tipo numérico inteiro.
print()
print(2**6)  # A função PRINT retorna a potência de dois elevado à sexta potência que é 64.
print()
print(36**(1/2))  # A função PRINT retorna a raiz quadrada de 36 que é 6. obs.: o índice deve estar entre parênteses.
print(type(36**(1/2)))  # A operação de radiciação retorna um tipo numérico flutuante.
print()
print(125**(1/3))  # A função PRINT retorna a raiz cúbica de 125 que é 5.
print()
print(round(125**(1/3)))  # Ao usarmos a função ROUND estaremos arredondando este número para 5, pois anteriormente
# não havia sido arredondado.
print(type(round(125**(1/3))))  # Round retornou inteiro.

