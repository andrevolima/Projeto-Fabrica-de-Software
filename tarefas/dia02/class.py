class Time:
    def __init__(self, nome, treinador, artilheiro):
        self.nome = nome
        self.treinador = treinador
        self.artilheiro = artilheiro

    def titulo(self):
        print("O time ganhou um titulo, a seguir o nome, titulo e artilheiro do time:", self.nome, self.treinador, self.artilheiro)

meu_time = Time("flamengo","tite","Pedro")
meu_time.titulo()    