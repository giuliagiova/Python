class Persona:
    def saluta(self):
        print("Ciao")

class Studente(Persona):
    def saluta(self):
        print("Ciao, sono uno studente!")

persona1 = Persona()
studente1 = Studente()
persona1.saluta()   #Output: Ciao!
studente1.saluta()     #Output: Ciao, sono uno studente!