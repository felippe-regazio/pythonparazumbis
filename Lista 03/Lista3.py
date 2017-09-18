# -*- coding: utf-8 -*-

# LISTA III

# ==============================================================================================
# FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS
# ==============================================================================================

# FUNCOES UTEIS PARA OS EXERCICIOS PYTHON PARA ZUMBIS
# Estas funções são rotinas muito utilizadas no exercicios, como receber apenas
# Numero Inteiros, Por exemplo. Se for utilizar, estude os codigos,

# Receber inteiro com verificação

def RecebeInteiro(i):
    i = 0
    while True:
      try:
         i = int(input(":: "))
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


def LimparTela():
  for i in range(0, 100):
      print("");
      return 0;

# Pause

def Pause():
    p = input("\nPressione <Enter> para continuar ...\n");
    return 0;


# ==============================================================================================
# EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS
# ==============================================================================================

# Exercicio 1

def Exercicio1(x):

    print("Por favor, digite um número entre 0 e 10")
    x = RecebeInteiro(x);

    if x > 10 or x < 0:
        print("Numero Inválido!")
        x = RecebeInteiro(x);
    else:
        print("\nVocê digitou o número "+str(x))
        return x;

# Exercicio 2

def Exercicio2():

    u = input("\nNome de Usuário :: ")

    while True:

        s = input(" \nSenha :: ")
        if s == u:
            print("\n\nA senha deve ser diferente do nome de usuário")
            print("Por favor digite outra senha")
            continue
        else:
            break;

    print("Obrigado!")
    return 0;

# Exercicio 3

def Exercicio3():

    a = 80000
    b = 200000
    ano = 0

    while a <= b:
    	a += a * 0.03
    	b += b * 0.015
    	ano += 1

    print ( "\nA ultrapassa ou iguala a B em %d anos\n" %ano )

# Exercicio 4

def renderFibonacci ( n ):

    a,b = 0,1
    for i in range( n ):
        a, b = b, a+b
    return a

def Exercicio4():

    L = 0 ; # Limite
    f = []; # RenderSequencia

    print("Digite um limite para a Sequencia Fibonacci: ")
    L = RecebeInteiro(L);

    for x in range(L):
        f.append( renderFibonacci(x) )
        print( f )

    print("\nF("+str(L)+") = "+str( f[ len(f) -2 ] ))
    print("Sua sequencia Fibonacci retornou "+str(len( f ))+" objetos na lista")

def Exercicio5():

    print("Bora calcular o MDC entre dois inteiros positivos utilizando Algoritmo de Euclides")

    print("\nDigite o primeiro Inteiro")
    # Verifica se 'a' é um inteiro Positivo
    a = 0;
    while True:
        a = RecebeInteiro(a)
        if a <= 0:
            print("\nDigite um valor positivo diferente de zero")
            continue
        else:
            break;

    print("\nDigite o segundo Inteiro")
    # Verifica se 'b' é um inteiro Positivo
    b = 0;
    while True:
        b = RecebeInteiro(b)
        if b <= 0:
            print("\nDigite um valor positivo diferente de zero")
            continue
        else:
            break;

    print("\nVocê escolheu "+str(a)+" , "+str(b));





# ==============================================================================================
# CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS
# ==============================================================================================

# EXERCICIO 1
a = 0;
a = Exercicio1(a);

# EXERCICIO 2
Exercicio2();

# EXERCICIO 3
Exercicio3();

# EXERCICIO 4
Exercicio4();

# EXERCICIO 5
Exercicio5();

#FelippeRegazio
