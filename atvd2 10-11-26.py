class Personagem:
    def __init__(self, nome, vida, poder):
        #Atributos
        self.nome = nome
        self.vida = vida
        self.poder = poder

    #Métodos
    def apresentar(self):
        print("------------")
        print("Personagem:", self.nome)
        print("Vida:", self.vida)
        print("Poder:", self.poder)

    def atacar(self, outro_personagem):
        print("")
        print(self.nome, "Atacou", outro_personagem.nome)
        outro_personagem.vida -= self.poder
        if outro_personagem.vida > 0:
            print("Vida restante:", outro_personagem.vida)
        else:
            print(outro_personagem.nome, "Foi derrotado!")

heroi = Personagem("Guerreiro", 100, 30)
vilao = Personagem("Dragao", 120, 20)
arqueiro = Personagem("Arqueiro", 90, 40)
mago = Personagem("Mago", 80, 50)
ladino = Personagem("Ladino", 100, 30)

heroi.apresentar()
vilao.apresentar()
arqueiro.apresentar()
mago.apresentar()
ladino.apresentar()

heroi.atacar(vilao)
arqueiro.atacar(mago)
mago.atacar(arqueiro)
ladino.atacar(vilao)
heroi.atacar(vilao)
mago.atacar(vilao)


