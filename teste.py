import os
os.system ('cls')

def tocar_musica (soma):
    musicas = [

        "cheia de manias",
        "deus me livre",
        "ciúme de você",
        "me leva junto com você",
        "é tarde demais",
        "quando te encontrei",
        "cigana"
    ]
    if 0 <= soma <= 6:
        print(f"a música que tocará é: {musicas[soma]}")
    else:
        print("soma fora do intervalo")

n1 = int(input("insira o primeiro número: "))
n2 = int(input("insira o segundo número: "))

soma = n1 + n2
tocar_musica(soma)
