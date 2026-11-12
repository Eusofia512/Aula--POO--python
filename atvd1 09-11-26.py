class Personagem:
    def __init__(self, nome, vida, poder):
        self.nome = nome
        self.vida = vida
        self.poder = poder

    def atacar(self):
        print(self.nome, "Atacou o inimigo!")

    def correr(self):
        print(self.nome, "O inimigo correu!")

    def mana(self):
        print(self.mana, "Sua mana acabou")

    def mirar(self):
        print(self.mirar, "Seu tiro foi um sucesso")

    def roubar(self):
        print()

    def apresentar(self):
        print("Nome:", self.nome)
        print("Vida:", self.vida)
        print("Poder:",self.poder)

#Criando objetos
personagem1 = Personagem("Guerreiro", 100, 50)
personagem2 = Personagem("Mago", 80, 90)
personagem3 = Personagem("Arqueiro", 100, 50)
personagem4 = Personagem("Ladino", 100, 60)
personagem5 = Personagem("Clerigo", 80, 90)
personagem6 = Personagem("Bárbaro", 100, 50)

#Chamando métodos
personagem1.apresentar()
personagem1.atacar()

personagem2.apresentar()
personagem2.atacar()
personagem2.mana()

personagem3.apresentar()
personagem3.atacar()
personagem3.mirar()

personagem4.apresentar()
personagem4.atacar()
personagem4.roubar()

personagem5.apresentar()
personagem5.atacar()

personagem6.apresentar()
personagem6.atacar()
personagem6.labia()