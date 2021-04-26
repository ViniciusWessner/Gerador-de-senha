#Mauisculas e Minusculas
#Numeros simbolos e espaços
#

"""
security = chave
5ecur1ty = senha

hexadecimais

1=1
2=2
até o 9=9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F



"""


chave = input("Digite sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "9"
    elif letra in "Cc": senha = senha + "3"
    elif letra in "Dd": senha = senha + "8"
    elif letra in "Ee": senha = senha + "2"
    elif letra in "Ff": senha = senha + "0"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    elif letra in "Vv": senha = senha + "@"
    else: senha = senha + letra
print(senha)