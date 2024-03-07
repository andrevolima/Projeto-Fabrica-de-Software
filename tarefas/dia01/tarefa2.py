num = int(input("Digite um numero: "))
i = 2

while i < num:
    if num % i == 0:
        break
    i += 1

if (i == num):
     print(f"{num} {'é um número primo.'}")
else:
    print('não é um número primo.')


