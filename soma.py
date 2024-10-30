import os
os.system ('cls')

soma=0
impar=0
for i in range(1, 501, 2):
    if i%3==0:
        soma = soma + i
        print(i, end=' ')

print("\na soma de todos os números é de: ", soma)
    
    
    
