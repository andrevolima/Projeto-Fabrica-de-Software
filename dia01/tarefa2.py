num = int(input("Digite um numero: "))
i = 2

while i < num:
    if num % i == 0:
        break
    i += 1

print(f"{num} {'é um número primo.' if i == num else 'não é um número primo.'}")