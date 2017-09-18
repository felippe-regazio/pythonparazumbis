# -*- coding: utf-8 -*-

# LISTA IV

# ==============================================================================================
# EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS EXERCICIOS
# ==============================================================================================

from random import randint


# gera numeros randomicos de 0 a 100 na lista a
def Exercicio1():

    a = [];

    for i in range (0, 10):
        a.append( randint( 0,100 ) );

    maxx = a[0]
    minn = a[0]

    for x in a:
        if x > maxx:
            maxx = x;
        if x < minn:
            minn = x;

    print ("Foram sorteados 10 valores de 0 a 100\nSendo eles", a)
    print ("\nMaior valor sorteado :: ", maxx, "\nMenor valor sorteado :: ", minn)

    return 0;


def Exercicio2():

    a, i, p = [], [], []

    for x in range (0, 20):

        n = randint( 0,100 )
        a.append( n )

        if n % 2 == 0:
            p.append( n )
        else:
            i.append( n )

    print ("Todos os Números: ", a, "\n\nPares: ", p, "\n\nÍmpares: ", i)
    return 0;


def Exercicio3():

    a, b, c = [], [], []

    for i in range (0, 10):

        a.append( randint( 0,100 ) )
        b.append( randint( 0,100 ) )
        # metodo mais simples de intercalar
        #c.append(a[i])
        #c.append(b[i])

    # Comente a linha abaixo
    # e descomente as linhas no for para modificar o medoto de intercalar
    c = list( sum( zip( a, b ), ()) )

    print( "Primeiro Vetor: \n", a, "\n\nSegundo Vetor : \n", b, "\n\nTerceiro Vetor: \n", c )


def Exercicio4():

    a = list( 'Python'.lower() )

    t = ''' The Python Software Foundation and the global Python
            community welcome and encourage participation by everyone. Our community is based on
            mutual respect, tolerance, and encouragement, and we are working to help each other live up
            to these principles. We want our community to be more diverse: whoever you are, and
            whatever your background, we welcome you. '''.lower().split()

    ws = []

    for x in t:
        #comeca com
        if x[:1:] in a:
            ws.append( x )
        #termina com
        if x[-1::] in a:
            ws. append( x )

    print ( "Palavras que começam ou terminam com alguma letra em 'Python': \n\n", ws )


def Exercicio5():

    a = list( 'Python'.lower() )

    t = ''' The Python Software Foundation and the global Python
            community welcome and encourage participation by everyone. Our community is based on
            mutual respect, tolerance, and encouragement, and we are working to help each other live up
            to these principles. We want our community to be more diverse: whoever you are, and
            whatever your background, we welcome you. '''.lower().split()

    ws = []

    for x in t:

        c = list(x)

        for l in a:
            if l in c: # se cada letra em l estiver contida em x splitado (c)
                ws.append(x);

    print( ws )

# ==============================================================================================
# CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS CHAMADAS
# ==============================================================================================

'''
Observação: Comente os exercicios que nao deseja ver a saida e mantenha apenas os que deseja
visualizar o resultado.

1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.
'''

Exercicio1()

'''
2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.
'''

Exercicio2()

'''
3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.
'''

Exercicio3()

'''
4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com
split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas.
'''

Exercicio4()

'''
5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.
'''

Exercicio5()

#FelippeRegazio
