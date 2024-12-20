class Auto:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrizione(self, velocita):
        return f"Auto: {self.marca} {self.modello} del {self.anno}. Velocità attuale: {velocita}"

    def aumentaVelocita(self, velocita, incremento):
        velocita += incremento
        return f"Velocità aumentata di {incremento} km/h. Velocità attuale: {velocita} km/h"   

    def diminuisciVelocita(self, velocita, decremento):
        velocita -= decremento 
        return f"Velocità diminuita di {decremento} km/h. Velocità attuale: {velocita} km/h"