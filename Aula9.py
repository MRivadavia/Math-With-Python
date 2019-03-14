

""""Criando uma tabuada da multiplicação"""


# Primeiramente, vamos construir a tabuada de um determinado número "mais simples".
# Perguntar ao usuário qual tabuada ele deseja criar.

a=int(input('Digite o número da tabuada que deseja criar:'))

print('Tabuada do ',a)
print()
print(a,'x 0 =',a*0)  # A função Print imprimirá na tela o valor digitado multiplicado
print(a,'x 1 =',a*1)
print(a,'x 2 =',a*2)
print(a,'x 3 =',a*3)
print(a,'x 4 =',a*4)
print(a,'x 5 =',a*5)
print(a,'x 6 =',a*6)
print(a,'x 7 =',a*7)
print(a,'x 8 =',a*8)
print(a,'x 9 =',a*9)
print(a,'x 10 =',a*10)

# Agora, vamos elaborar um pouco mais a tabuada.

a=int(input('Digite o número da tabuada que deseja criar:'))

print('Tabuada do ',a)
print()
for k in range(11):
    print(a, 'x', k ,'=', a * k)  # A função Print imprimirá na tela o valor digitado multiplicado

# Outra maneira de resolvermos ou apresentarmos em tela esta tabuada é:

a=int(input('Digite o número da tabuada que deseja criar:'))

print('Tabuada do ',a)
print()
for k in range(11):  # É construido um laço For de 0 a 10 para a função abaixo repetir.
    print('{0} x {1} = {2}'.format(a,k,a*k))  # A função Format é usada para formatação de saídas de dados.
    # Os valores entre chaves e postos em ordem crescente estão relacionados aos parametros da função Format
    # respectivamente.  O zero entre chaves recebe o valor da variável 'a', o um entre chaves recebe o valor da
    # variável 'k' e o dois entre chaves recebe o valor do produto entre as variáveis 'a' e 'k'.



