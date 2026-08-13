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

'''---------------------------------------------------problema 3---------------------------------------------'''

