

n1 = int(input("Digite a nota do aluno: "))
n2 = int(input("Digite a nota do aluno: "))
n3 = int(input("Digite a nota do aluno: "))
 

def Soma(x, y, z):

    soma = x + y + z

    return soma

def media_aluno(b):
  
    media = b / 3

    return media

print(f"A soma dos 3 numeros e: {Soma(n1, n2, n3)}")
print(f"A soma dos 3 numeros e: {media_aluno(Soma(n1,n2,n3))}")

      