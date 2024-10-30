import os 
os.system ('cls')

matriz = [[], [], []]
soma = 0

for l in range(3):
    for c in range(3):
        num = int(input(f"insira os valores para [{l}] [{c}]: "))
        matriz[l].append(num)
#colunas depende de LINHAS

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]}]", end = " ")
    print()
            
print("Números matriz secundária: ")
for l in range(3):
    for c in range(3):
        if l + c == 2:
            soma += matriz[l][c]
            print(f"[{matriz[l][c]}]", end = " ")
        

print(f"\nA soma da diagonal secundária é: {soma}")



