import os 
os.system ('cls')

matriz = [[], [], []]
soma = 0 
soma_linha3 = 0 

for l in range(3):
    for c in range(3):
        num = int(input(f"insira um valor para [{l}][{c}]: "))
        matriz[l].append(num)
#l e c são os índices da matriz, NÃO OS VALORES

for l in range(3):
    for c in range(3):
        soma += matriz[l][c]
        print(f"[{matriz[l][c]}]", end = " ")
        
    print()

print("Elementos da diagonal principal: ")
for l in range (3):
    for c in range (3):
        if l == 2 :
            soma_linha3 += matriz[l][c]
#precisa dos índices (linha e coluna)
        if l == c :
            print(f"[{matriz[l][c]}]")

print("MATRIZ TRANSPOSTA:")
for l in range (3):
    for c in range (3):
        print(f"[{matriz[c][l]}]", end = " ")
    
    print()
            
    
print(f"A soma dos elementos da ultima línha é: {soma_linha3}")
print(f"A soma de todos os elementos é: {soma}")


