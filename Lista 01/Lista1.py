# ==============================================================================================
# FUNCOES UTEIS

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

# Pause

def Pause():
    p = input("\nPressione <Enter> para continuar ...\n");

# Receber inteiro com verificação

def RecebeInteiro(i):
    i = 0
    while True:
      try:
         i = int(input("Por favor, digite um valor inteiro: "))
      except ValueError:
         print("Valor não inteiro!\n")
         continue
      else:
         print("Obrigado\n")
         break
    return i;

# Receber float com verificação

def RecebeFloat(i):
    i = 0
    while True:
      try:
         i = float(input("Por favor, digite um valor numérico: "))
      except ValueError:
         print("Valor não inteiro!\n")
         continue
      else:
         print("Obrigado\n")
         break
    return i;

# ==============================================================================================
# EXERCICIOS

LimparTela();

def pythonMassa():
    Massanori();
    Pause();
    LimparTela();

# SOMA INTEIROS

def somaInteiros():
    print("========================================\n")
    print("Programa que soma dois números inteiros\n\n");

    a = 0;
    a = RecebeInteiro(a);

    b = 0;
    b = RecebeInteiro(b);

    print("\nA soma dos valores inseridos é igual a: "+str(a+b)+"\n");

    Pause();
    LimparTela();

# CONVERTE METROS PARA MM

def mtoMM():

    a = 0;

    print("========================================\n")
    print("Programa que converte Metros para Milímetros\n\n");

    a = RecebeInteiro(a);
    print(str(a)+" Metros é igual a: "+str(a * 1000)+" mm");

    Pause();
    LimparTela();

# DIA + HORA + MINUTO + SEGUNDO  PARA SEG.

def dHMStoS():
    print("========================================\n")
    print("Receberemos a quantidade Dias\Horas\Minutos\Segundos e retornaremos o valor em segundos\n\n");

    d = 0;
    print("\nNUMERO :: DIAS");
    d = RecebeInteiro(d);

    h = 0;
    print("\nNUMERO :: HORAS");
    h = RecebeInteiro(h);

    m = 0;
    print("\nNUMERO :: MINUTOS");
    m = RecebeInteiro(m);

    s = 0;
    print("\nNUMERO :: SEGUNDOS");
    s = RecebeInteiro(s);

    # printa o resultado

    print("O valor de D "+str(d)+" :: H "+str(h)+" M "+str(m)+" :: "+str(s)+" :");
    print(str(( d * 86400) + (h * 3600) + (m * 60) + s )+" segundos");

    Pause();
    LimparTela();

# PROGRAMA QUE CALCULA SALARIO

def aumentaSalario():
    print("========================================\n")
    print("Este programa calculara um aumento simples em %");

    s = 0;
    print("\n$$ VALOR DO SALÁRIO");
    s = RecebeInteiro(s);

    p = 0;
    print("\n%% PORCENTAGEM A SER INCLUSA NO SALARIO");
    p = RecebeInteiro(p);

    print(str(s)+" Com aumento de "+str(p)+"% será igual a: "+str(s + s * p / 100));

    Pause();
    LimparTela();

# PROGRAMA QUE CALCULA DECREMENTACAO DE DESCONTO

def calculaDesconto():
    print("========================================\n")
    print("Este programa calculara o desconto de algum produto %");

    p = 0;
    print("\n$$ VALOR DO PRODUTO");
    p = RecebeInteiro(p);

    d = 0;
    print("\n%% VALOR DO DESCONTO");
    d = RecebeInteiro(d);

    print("Um produto de valor "+str(p)+" reais com "+str(d)+"% de desconto é igual a: "+str(p - p * d / 100));

    Pause();
    LimparTela();

# PROGRAMA QUE CALCULA O TEMPO DE VIAGEM

def tempoDeViagem():
    print("========================================\n")
    print("Este programa calculara o tempo medio de uma viagem");

    km = 0;
    print("\nQUANTOS KM VOCE IRA VIAJAR?");
    km = RecebeInteiro(km);

    v = 0;
    print("\nA QUE VELOCIDADE MEDIA EM KM/H?");
    v = RecebeInteiro(v);

    print("Viajando há "+str(v)+" km por hora, por "+str(km)+" quilometros, você demorará "+str(km / v)+" horas para chegar");

    Pause();
    LimparTela();

# CONVERTE TEMPERATURA DE C PARA F E O CONTRARIO

def CtoF():
    print("========================================\n")
    print("Este programa converte Celsius para Fahrenheit");

    c = 0;
    print("\nQUANTOS GRAUS EM C VC DESEJA CONVERTER PARA F?");
    c = RecebeInteiro(c);

    print(str(c)+"C em Fahrenheit = "+str( (c + 32) / 1.8 ));

    Pause();
    LimparTela();

def FtoC():
    print("========================================\n")
    print("Este programa converte Fahrenheit para C");

    f = 0;
    print("\nQUANTOS GRAUS EM F VC DESEJA CONVERTER PARA C?");
    f = RecebeInteiro(f);

    print(str(f)+"F em Celsius = "+str( (f * 1.8) -32 ));

    Pause();
    LimparTela();

# CALCULO PARA CARRO ALUGADO

def carroAlugado():
    print("========================================\n")
    print("Este programa calcula valores a pagar de um carro alugado");

    d = 0;
    print("\nQUANTOS DIAS VOCE FICOU COM O CARRO?");
    d = RecebeInteiro(d);

    km = 0;
    print("\nQUANTOS KM VOCE PERCORREU COM O CARRO?");
    km = RecebeInteiro(km);

    valor = d * 60+km * 0,15;
    print( "Você deve pagar ${0}".format(valor) );

    Pause();
    LimparTela();

# FUMANTE

def fumanteCount():
    print("========================================\n")
    print("Este programa calcula quanto tempo de vida um fumante perdeu no cigarro");

    a = 0;
    print("\nHÁ QUANTOS ANOS VOCE FUMA?");
    a = RecebeInteiro(a);

    c = 0;
    print("\nQUANTO CIGARROS POR DIA VC FUMA?");
    c = RecebeInteiro(c);

    print( "Você perdeu "+str( (365 * a) * (c * 10) )+" minutos de vida para o cigarro");

    Pause();
    LimparTela();

# NUMERO DE DIGITOS DE 2 ^ 1 * 10 ^ 6

def elevateCount():
    print("========================================\n")
    print("Programa que conta o numero de digitos contido em 2 elevado a 1 milhao");

    print("\n2 elevado a 1 milhao possui o seguinte numero de digitos:")
    print(len(str(2 ** 1000000)))
    Pause();
    LimparTela();


# ==============================================================================================
# MENU -- CHAMA CADA SOFTWARE DE ACORDO COM O MENU

def softwareMenu():

    LimparTela();

    s = 0;

    print('QUAL SOFTWARE VOCE DESEJA EXECUTAR?');
    print('');

    print(' 1 - Massanori Function');
    print(' 2 - Soma Inteiros');
    print(' 3 - Converte M to MM');
    print(' 4 - Dia + Hora + Min + Seg para Seg');
    print(' 5 - Aumenta Salário');
    print(' 6 - Decrementa Desconto');
    print(' 7 - Tempo de Viagem');
    print(' 8 - Celsius para Fahrenheit');
    print(' 9 - Fahrenheit para Celsius');
    print('10 - Carro Alugado');
    print('11 - Fumante');
    print('12 - Conta Dígitos');

    print("");

# chama a funcao de acordo com a opcao escolhida pelo user

    s = RecebeInteiro(s);

    if ( s == 1 ):
        pythonMassa();

    if ( s == 2 ):
        somaInteiros();

    if ( s == 3 ):
        mtoMM();

    if ( s == 4 ):
        dHMStoS();

    if ( s == 5 ):
        aumentaSalario();

    if ( s == 6 ):
        calculaDesconto();

    if ( s == 7 ):
        tempoDeViagem();

    if ( s == 8 ):
        CtoF();

    if ( s == 9 ):
        FtoC();

    if ( s == 10 ):
        carroAlugado();

    if ( s == 11 ):
        fumanteCount();

    if ( s == 12 ):
        elevateCount();

# se s não estiver no range de 0 a 12 (opcoes) sai

    if ( s not in range(0,12) ):
        exit;


softwareMenu();

#FelippeRegazio
