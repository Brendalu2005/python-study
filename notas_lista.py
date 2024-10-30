import os
os.system ('cls')

notas_total = []
for i in range (10):
    nota = int(input("Insira nota do aluno: "))
    if nota < 0 or nota > 10:
        print("Erro") 
    else:
        notas_total.append(nota)
media = sum(notas_total)/10
print(notas_total)
print(f"A média de todas as notas é de: {media}")
print(f"A nota máxima foi de {max(notas_total)}, e a menor nota foi de {min(notas_total)}")
print("Notas acima da média: ")
for n in notas_total:
    if n > media:
        print(n, end = " ")
