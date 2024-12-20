class Persona:
    Specie = "Homo Sapiens"     #Attributo di classe

    def __init__(self, nome, eta):
        self.nome = nome                 #Attributo di istanza
        self.eta = eta

persona1 = Persona("Mario", 30)
print(persona1.Specie)  #Output: Homo sapiens
print(persona1.nome)  #Output: Mario


    








    
