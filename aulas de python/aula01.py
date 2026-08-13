'''logica de programaçao'''


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



























media_alunos()



