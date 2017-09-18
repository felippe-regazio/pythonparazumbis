# -*- coding: utf-8 -*-

# ==============================================================================================
# FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS FUNCOES UTEIS
# ==============================================================================================

# FUNCOES UTEIS PARA OS EXERCICIOS PYTHON PARA ZUMBIS
# Estas funções são rotinas muito utilizadas no exercicios, como receber apenas
# Numero Inteiros, Por exemplo. Se for utilizar, estude os codigos,

# Funcao de Abertura | Massanori

def Massanori():
    print("\nPython é Legal\n");
    return 0;

# Limpar a Tela

def LimparTela():
  for i in range(0, 100):
      print("");
      return 0;

# Pause

def verificaMaior(a):

    currmax = a[0];
    for i in range (0, len(a)):
        if a[i] >= currmax:
            currmax=a[i];

    return(currmax)

def verificaMenor(a):

    currmin = a[0];
    for i in range (0, len(a)):
        if a[i] <= currmin:
            currmin=a[i];

    return(currmin)

def Pause():
    p = input("\nPressione <Enter> para continuar ...\n");
    return 0;

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


# ==============================================================================================
# EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS
# ==============================================================================================


# FUNCAO QUE VERIFICA SE O TRIANGULO EH EQUILATERO, ISOCELES OU ESCALENO

def VerificaTriangulo():

    print("============================================")
    print("Programa que verifica o tipo de triangulo: \n\n")

    tipo = "i"

    print("LADO A: ")
    a = 0
    a = RecebeInteiro(a)

    print("LADO B: ")
    b = 0
    b = RecebeInteiro(b)

    if a != b:
        tipo = "x"

    print("LADO C: ")
    c = 0
    c = RecebeInteiro(c)

    if c != ((a + b) / 2):
        tipo = "x"

    # result # se nao e escaleno nem equilatero, so pode ser isoceles

    if tipo == "i":
        print("Triangulo Equilatero!")

    elif ( a != b ) and ( a != b ):
        print("Triangulo Escaleno!")

    else:
        print("Triangulo Isóceles!")

    Pause();
    LimparTela();

# FUNCAO QUE VERIFICA SE O ANO EH BISEXTO

def verificaBissexto():

    a = 0;
    print ("Por favor, digite o ano que deseja verificar: ");
    a = RecebeInteiro(a);

    #primeira situacao, deve ser divisivel por 4 e nao divisivel por 100

    if ( a % 4 == 0 ) and ( a % 100 != 0 ):

        print("\nAno bissexto!\n")

    elif ( a % 4 != 0 ) and ( a % 400 == 0 ):

        print("\Ano Bissexto!\n")

    else:

        print("\nAno não é bissexto\n")

    Pause();
    LimparTela();


# FUNCAO QUE VERIFICA KILOS EXCEDENTES EM PESCA

def verificaPeixe():

    print ("Por favor, digite o peso da mercadoria (4,00 de multa por KG excedente): ");

    p = 0;
    p = RecebeFloat(p);

    if p <= 50:

        print("Não houve cobrança de multa")

    else:

        m = ( p - 50 ) * 4
        print("Você pagará: %6.2f de multa." %m)

# VERIFICA MAIOR NUMERO NUMA LISTA =============================================

def MaiordeTres():

    print("\nVamos calcular o maior numero de tres\n")

    a = int(input("NUM 1: "))
    b = int(input("NUM 2: "))
    c = int(input("NUM 3: "))

    print("\nO maior número digitado foi:\n");
    print(verificaMaior([a,b,c]))
    return 0;

def MaiorMenordeTres():

    print("\nVamos calcular o menor numero de tres\n")

    a = int(input("NUM 1: "))
    b = int(input("NUM 2: "))
    c = int(input("NUM 3: "))

    print("\nO maior número digitado foi:\n");
    print(verificaMaior([a,b,c]))

    print("\nO menor número digitado foi:\n");
    print(verificaMenor([a,b,c]))
    return 0;

def CalculaSalario():

    print("\nVamos calcular os tributos do seu salário?")
    print("Por favor, digite quanto você ganha por hora\n")
    h = 0
    h = RecebeFloat(h)

    print("Por favor, digite seu numero de horas trabalhadas no mês\n")
    n = 0
    n = RecebeFloat(n)

    # salario
    s = h * n

    # imposto - 11%
    imp = s - (s - s * 11 / 100)

    # inss - 8%
    ins = s - (s - s * 8 / 100)

    # sindicato - 5%
    sin = s - (s - s * 5 / 100)

    print( "\nIMPOSTO" )
    print(imp)

    print( "\nINSS" )
    print(ins)

    print( "\nSINDICATO" )
    print(sin)

    print( "\nSALÁRIO BRUTO" )
    print(s)

    print( "\nSALÁRIO LÍQUIDO" )
    print( s - imp - ins - sin )

def CalculaTinta():

    print("Digite o Tamanho da Área a ser Pintada: ")

    a = 0
    a = RecebeInteiro(a)

    # 1L = 3M
    l = a * 3  #quantos litros serao necessarios

    b = l / 18 # quantidade de latas

    if b < 1:
        b = 1

    v = b * 80 # valor

    print ("Você precisará de "+str(b)+" latas de 18L e pagará "+str(v)+" reais");

# ==============================================================================================
# CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS
# ==============================================================================================


# Exercicio 1
VerificaTriangulo();

# Exercicio 2
verificaBissexto();

# Exercicio 3
verificaPeixe();

# Exercicio 4
MaiordeTres()

# Exercicio 5
MaiorMenordeTres()

# Exercicio 6
CalculaSalario()

# Exercicio 7
CalculaTinta()


#FelippeRegazio
