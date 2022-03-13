n = int(input("Digite o valor de n: "))
i = n - 1

if(n == 0):
    n = 1
else:
    while (i != 0):
        n = i * n
        i = i - 1

print(n)