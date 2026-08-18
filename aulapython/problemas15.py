'''logica de programaçao'''

''''problema 1'''



def media_alunos():

    nome = input( "digite seu nome: ")
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    nota3 = float(input("digite sua terceira nota: "))
    nota4 = float(input("digite sua quarta nota: "))
    nota5 = float(input("digite sua quinta nota: "))

    media = (nota1 + nota2 + nota3 + nota4 + nota5 ) / 5

    if media < 4:

        print(f"{nome} sua media e {media} voce nao foi aprovado")

    elif media >= 4  and media <= 6 :

        print(f"{nome} sua media e {media} voce esta de recuperaçao")

    elif media >=6 and media <= 9:
    
            print(f"{nome} sua media e {media} voce foi aprovado")
    
    elif media > 9:
        print(f"{nome} sua media e {media} voce foi aprovado com destaque")


'''chamar a funçao'''


'''media_alunos()'''

'''-------------------------------------------problema 2 ---------------------------------------------------------'''
def ano():

    ano = int(input("digite o ano exemplo 1900, 2000 e etc: "))


    if ano % 400 == 0:
        print(f"{ano} e bissexto")

    elif ano % 4 == 0 and ano % 100 != 0:
        print(f"{ano} bissexto")

    elif ano % 100 == 0 and ano % 400 != 0:
        print(f"{ano} bissexto")

    else:
        print("ano nao bissexto")
        

'''ano()'''

'''-------------------------------------------problema 3 ---------------------------------------------------------'''
def maior_numero():
    a = int(input("digite o primeiro numero: "))
    b = int(input("digite o segundo numero: "))
    c = int(input("digite o terceiro numero: "))

    if a == b and a == c:
        print("todos os numeros sao iguais")
    else:
        if a > b and a > c:
            maior = a
        elif b > a and b > c:
            maior = b
        elif c > a and c > b:
            maior = c

        if a <= b and a <= c:
            menor = a
        elif b <= a and b <= c:
            menor = b
        elif c <= a and c <= b:
            menor = c

        print ("maior numro é:" ,maior)
        print ("menor numero é:" ,menor)

'''maior_numero()'''


'''---------------------------------------------------problema 4---------------------------------------------'''

def boolll():

    numero = int(input("digite um numero: "))

    entre = numero >= 10 and numero <= 50
    par = numero % 2 == 0 
    atendedois = entre and par

    if atendedois == True:
        print(f"{numero} esta entre 10 e 50 e é par")
    elif entre == False and par == True:
        print(f"{numero} não esta entre 10 e 50 e é par")
    elif entre == True and par == False:
        print(f"{numero} esta entre 10 e 50 e não é par")
    else:
        print(f"{numero} não esta entre 10 e 50 e não e par")
    
'''boolll()'''

'''---------------------------------------------------problema 5---------------------------------------------'''

def contagem():

    numero = int(input("digite um numero: "))

    while numero >= 0 :
        if numero > 0 and numero % 5 == 0:
            print(f"{numero} é divisivel por 5")
        else:
            print(f"{numero}")

        numero -= 1

'''contagem()'''