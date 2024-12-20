from ClasseAuto import Auto

velocita = 80
# Creazione di un oggetto della classe Auto
ferrari488 = Auto("Ferrari", "488", 2023)
lamborghiniHuracan = Auto("Lamborghini", "Huracàn", 2021)

# Descrizione iniziale dell'Auto
print(ferrari488.descrizione(velocita))
print(lamborghiniHuracan.descrizione(velocita))

# Aumento della velocità
incremento = int(input("Inserisci l'incremento di velocità per la Ferrari 488: "))
print(ferrari488.aumentaVelocita(velocita, incremento))

# Diminuzione della velocità
decremento = int(input("Inserisci il decremento di velocità la Ferrari 488: "))
print(ferrari488.diminuisciVelocita(velocita, decremento))