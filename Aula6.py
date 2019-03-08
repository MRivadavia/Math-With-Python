
""""Programa que manipula com Exceçöes quanto ao tipo de Dados de Entrada ou Saída"""


try:
    a = int(input('Entre com um valor inteiro:'))  # Se receber um valor inteiro, será printado na tela a soma correta.
    try:
        print('A soma de', a, 'mais', a, 'é igual a: ', a + a)
    except ValueError:
        pass  # Instrução que não realiza nenhuma operação.
except ValueError:  # Se Input receber um valor de ponto flutuante ou uma String o Python abrirá uma exceção e teremos
    print('Entre com um valor inteiro correto!')  # uma saída exigindo a entrada de dados correta.

try:
    x = int(input('Entre com um valor inteiro: '))
    y = 10 / x
    print('O quociente da Divisão é: ', y)  # Será printado na tela se a entrada de dados for Inteiro.
except ZeroDivisionError:  # Abrirá uma exceção se a entrada for o número Zero.
    print('Divisão por Zero!')
except ValueError:  # Abrirá uma exceção se a entrada de dados for ponto flutuante ou String.
    print('Tipo de dado Incompatível!')


try:
    x = float(input('Entre com um valor decimal: '))
    y = 10 / x
    print('O quociente da Divisão é: ', y)  # Será printado na tela se a entrada de dados for Inteiro.
except ZeroDivisionError:  # Abrirá uma exceção se a entrada for o número Zero.
    print('Divisão por Zero!')
except ValueError:  # Abrirá uma exceção se a entrada de dados for ponto flutuante ou String.
    print('Tipo de dado Incompatível!')


print('Determinando a velocidade do móvel')
t = float(input('Insira o tempo de percurso: '))  # A entrada de dados é feita antes do bloco de instruções Try.
try:
    v = 500 / t  # Se o tipo de dados for inserido corretamente, não uma String e nem Zero, esta fórmula
    # será calculada.  Se não, não será executada e abrirá a exceção descrita no código abaixo.
    # Mas se houver uma entrada de dados como String, será aberta uma exceção ValueError que não pode
    # converter String em ponto flutuante.
except ZeroDivisionError:
    print('Divisão por Zero!')  # Caso haja na variável 't' armazenamento do valor Zero.
finally:
    print('A velocidade é: ', v)  # Caso o valor da variável 't' seja um valor válido, o valor da
    # velocidade será impresso na tela, porém com erro desta variável 'v' não ter sido declarada e é aberta
    # uma exceção NameError.
# Para contornar estes possíveis erros, aperfeiçoaremos o código, como se mostra abaixo.



print('Determinando a velocidade do móvel')  # Título do problema.
try:  # Bloco Try, testa um sequëncia de códigos para avaliar possíveis erros.
    t = float(input('Insira o tempo de percurso: '))  # Entrada de valores do tipo flutuante.
    try:  # Bloco Try inserido em outro Try para que o erro de variável não declarada não seja um impedimento
        # para execução do programa.
        v = 500 / t  # Fórmula para determinar a velocidade de um móvel.
        print('A velocidade é: ', v)  # Quando os dados de entrada estão sem erros é impressa na tela a velocidade.
    except ValueError:  # Bloco que permite manipular os possíveis erros, identificar as exceções geradas e printar
        # na tela uma mensagem de aviso com respeito ao erro gerado.  ValueError é uma exceção gerada quando a função
        # usada for para um tipo de dados, mas o argumento tem valores especificados inválidos.
        print(t,' não pode ser convertido em ponto flutuante')
    except ZeroDivisionError:  # ZeroDivisionError é uma exceção gerada quando o argumento inserido gerar uma divisão
        # por zero. É printada na tela o aviso: Divisão por zero.
        print('Divisão por Zero!')
except ValueError:
    print('Entre com um valor numérico válido! ')
