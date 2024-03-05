list_num = [5, 8, 12, 20]
print("O terceiro elemento da lista e: ", list_num[2])


list_ft =[1.7, 2.8, 5.5, 12.2]
print("O segundo elemento da lista e: ", list_ft[1])


times =  {
    {"time":"Flamengo", "golspt":"23"},
    {"time":"Gremio", "golspt":"9"},
    {"time":"Palmeiras", "golspt":"17"},
    {"time":"Vasco", "golspt":"21"}
}
print(times)


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

sinal = input("Escolha entre soma (+) ou subtracao (-): ")

if sinal == "+":
    print(num1 + num2)
elif sinal == "-":
    print(num1-num2)
else:
    print("Sinal invalido")