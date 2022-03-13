"""Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo."""

n = int(input("Digite o valor de n: "))
impar = 1

while(n != 0):
    print(impar)
    impar = impar + 2
    n = n - 1