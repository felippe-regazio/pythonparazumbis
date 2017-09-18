# -*- coding: utf-8 -*-

# LISTA III

# ==============================================================================================
# FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS
# ==============================================================================================

def RecebeInteiro(i):
    i = 0
    while True:
      try:
         i = int(input("\n:: "))
      except ValueError:
         print("Valor não inteiro!\n")
         continue
      else:
         break
    return i;

# Receber float com verificação

def RecebeFloat(i):
    i = 0
    while True:
      try:
         i = float(input(":: "))
      except ValueError:
         print("Valor não numerico!\n")
         continue
      else:
         break
    return i;

# algoritmo babilonio para checar se um inteiro é um quadrado perfeito
# funciona com qualuer i+ que seu pc tenha poder de processamento pra calcular
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

# ==============================================================================================
# EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS
# ==============================================================================================

# x é triangular se 8x + 1 = y & y é um quadrado perfeito
# Lembrete: numeros terminados em 2, 3, 7, ou 8 nunca geram quadrados perfeitos

def Desafio1():

    # recebe um inteiro maior que 0
    print ("Digite um numero inteiro maior que Zero e checaremos se este é Triangular: \n")
    a = 0;
    while True:
        a = RecebeInteiro(a)
        if a > 0:
            break

    # resolve a formula para o obter o numero de teste

    b = 8 * a + 1

    # verifica se o num termina com 2, 3, 7 ou 8 utilizando string slices
    test = ['2','3','7','8']
    c = str(b)[-1:]

    if c in test:
        print( "\n", a, "Não é um número Triangular");
        return 0;

    # se 'b' for um quadrado perfeito, então 'a' é triangular
    if is_square(b): # is_square é uma funcao declarada acima nesse mesm code
        print( "\n", a, "é um número Triangular!");
    else:
        print( "\n", a, "Não é um número Triangular");

def Desafio2():

    # declara os valores

    valor = 0
    resto = 0
    notas = [ 100, 50, 20, 10, 5, 2 ]

    # recebe o valor a ser sacado
    print("\nNotas Disponíveis :: "+str(notas) )
    print("\nQuanto deseja sacar?\n")

    valor = RecebeFloat(valor)

    # declara os valores para computo das notas
    result = []
    i = 0

    # retira os centavos do valor
    valor, resto = divmod( valor, 1 )

    # se o numero for impar decrementa 1 e adiciona ao resto para garantir divisao exata
    if int(valor) % 2 != 0:
        valor -= 1
        resto += 1

    # conta as quantas notas retornar
    while valor > 0:


        n     = valor / notas[i]
        valor = valor % notas[i]

        if int(n) > 0:
            result.append( '\n %d Notas de R$ %.2f' %(n, notas[i]) )

        if valor <= 0:
            break
        else:
            i += 1

    # adiciona os centavos
    result.append( '\n Mais R$ %.2f em moedas' %resto );

    # mostra os resultados
    for i in range( 0, len(result) ):
        print( result[i] )

def Desafio3():

    check = 0
    n = 0

    while True:
        n = RecebeInteiro( n )
        if n > 0:
            break

    print( "\n" )

    if n == 2 or n == 3:
        print( n, "é primo!!!" )
        return 0;

    if n < 2 or n % 2 == 0:
        print( n, "não é primo" )
        return 0;

    if n < 9:
        print( n, "é primo!!!" )
        return 0;

    if n % 3 == 0:
        print( n, "não é primo!!!" )
        return 0;

    a = int( n ** 0.5 )
    x = 5

    while x <= a:
        print( x, ' , ')

        if n % x == 0:
            check = 0;
            break;

        if n % ( x + 2 ) == 0:
            check = 0;
            break;

        x += 6

    check = 1;

    print( "\n" )

    if ( check == 1 ):
        print( n, "é primo!!!" )
    else:
        print(n, "não é primo")

    return 0

def Desafio6():

  n = 0;
  while True:
      n = RecebeInteiro( n )
      if n > 0:
          break;

  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print ( '\t',f )
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def Desafio4():

    print("Por favor, digite um número inteiro positivo\n")

    n = 0
    while True:
        n = RecebeInteiro(n)
        if n > 0:
            break;

    quocientes = []
    divisores  = []

    while n > 1:

        # se <= 9 eh dividido por ele mesmo
        if n <= 9:
            quocientes.append( n )
            divisores.append( n )
            n = n / n
            # print(n)


        # se > 9 e par
        if n > 9 and n % 2 == 0:
            quocientes.append( n )
            divisores.append( 2 )
            n = n / 2
            # print(n)

        elif n > 9 and n % 2 != 0:
            quocientes.append( n )
            divisores.append( 3 )
            n = n / 3
            # print(n)

    print( "\nCocientes :", quocientes )
    print( "\nDivisores Primos :", divisores )
    print( "\n\n" )

    return 0

def Desafio5():

    a = 0
    a = RecebeFloat(a)

    print( '\n', a, "ao contrário = ", str(a)[::-1] )


# ==============================================================================================
# CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS
# ==============================================================================================

# Comente as execuções desenecessárias para executar expecificamente um Desafio1

'''
1. Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.
'''

#Desafio1();


'''
2. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
'''

Desafio2();

'''
3. Verifique se um inteiro positivo n é primo.
'''

#Desafio3();

'''
4. Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.
'''

#Desafio4();

'''
5. Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
'''

#Desafio5();

#FelippeRegazio
