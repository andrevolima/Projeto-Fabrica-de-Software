class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        
    def truque(self):
        print("O seu Animal aprendeu um truque", self.nome, self.raca)

   

class Barulho(Animal):
    def som(self):
       if (self.raca == "cachorro"):
        print(f"Seu cachorro {self.nome} faz auau")
       elif(self.raca == "gato"):
        print(f"Seu gato {self.nome} faz miau")
       else:
          print("esse animal nao e reconhecido")


meu_animal = Barulho("lili","cachorro")
dog_vizinho = Barulho("rex","cavalo")
cat_amigo = Barulho("tilapia", "gato")

meu_animal.som()
meu_animal.truque() 
print("")
dog_vizinho.som()
dog_vizinho.truque()
print("")
cat_amigo.som()
cat_amigo.truque()
print("")




    
