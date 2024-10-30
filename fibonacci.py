import os
os.system ('cls')

F = [0,1]
#começa sempre com zero e um
for i in range (2, 61):
    F.append(F[i-1] + F[i-2])
#O intervalo não pode começar em 1 ou em 0, porque dá um número negativo, gerando erro no índice
#O número de fibonacci é sempre a soma dos dois números anteriores a ele
#f[i-1]: primeiro número anterior a ele
#f[i-2]: segundo número anterior a ele

T = int(input("Insira a quantidade de números da sua lista: "))

for i in range (T):
    N = int(input("digite um número: "))
    print(f"Fib({N}) = {F[N]}")
    
#Lista[indice]: Mostra o valor a partir do indice da lista. 
