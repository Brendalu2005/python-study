import os
os.system ('cls')

lista_jogo = []
jogo = {}

for i in range (4):
    print("jogador 1 \njogador 2 \njogador 3 \njogador 4 ")
    jogo['jogador'] = str(input("insira que jogador você é: "))
    jogo['dado'] = int(input(f"insira o numero do dado do {jogo['jogador']} : "))
    if 0 < jogo['dado'] >=6:
        lista_jogo.append(jogo.copy())
    elif jogo['dado'] < 0:
        print("valor não permitido")

print(lista_jogo)

#fazer depois
